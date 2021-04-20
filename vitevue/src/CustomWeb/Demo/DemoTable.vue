<template>
  <div>
    <div class="table-operations">
      <a-button @click="filterOpen">Filter</a-button>
      <a-button >Create</a-button>
      <a-button >Delete</a-button>
      <a-button >Export</a-button>
    </div>
    <a-table
      :columns="table.columns"
      :data-source="table.data"
      :pagination="table.pagination"
      :scroll="table.scroll"
      :loading="table.loading"
      size="small"
      @change="handleTableChange"
      rowKey="id"
      :customRow="customRow"
      :customHeaderRow="customHeaderRow"
      :row-selection="rowSelection"
    >
      <template #action="item">
        <a-button @click="() => clickId(item)">{{ item.text }}</a-button>
      </template>
    </a-table>
    <a-drawer title="Filters" :width="480" :visible="filter.visible" :body-style="{ paddingBottom: '80px' }" @close="filterClose">
      <a-form :model="filter.form" :rules="filter.rules" layout="vertical">
        <a-form-item label="Name" name="name">
          <a-input v-model:value="filter.form.name" placeholder="Please enter user name" />
        </a-form-item>
        <a-form-item label="Owner" name="owner">
          <a-select placeholder="Please a-s an owner" v-model:value="filter.form.owner">
            <a-select-option value="xiao">Xiaoxiao Fu</a-select-option>
            <a-select-option value="mao">Maomao Zhou</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Type" name="type">
          <a-select placeholder="Please choose the type" v-model:value="filter.form.type">
            <a-select-option value="private">Private</a-select-option>
            <a-select-option value="public">Public</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Approver" name="approver">
          <a-select placeholder="Please choose the approver" v-model:value="filter.form.approver">
            <a-select-option value="jack">Jack Ma</a-select-option>
            <a-select-option value="tom">Tom Liu</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="DateTime" name="dateTime">
          <a-date-picker v-model:value="filter.form.dateTime" style="width: 100%" :get-popup-container="trigger => trigger.parentNode" />
        </a-form-item>
        <a-form-item label="Description" name="description">
          <a-textarea v-model:value="filter.form.description" :rows="4" placeholder="please enter url description" />
        </a-form-item>
        <h1 v-for="n of 8" :key="n">AAA</h1>
      </a-form>
      <div
        :style="{
          position: 'absolute', right: 0, bottom: 0, width: '100%', borderTop: '1px solid #e9e9e9', padding: '10px 16px', background: '#fff', textAlign: 'right', zIndex: 1,
        }"
      >
        <a-button style="margin-right: 8px" @click="filterClose">Cancel</a-button>
        <a-button type="primary" @click="filterApply">Submit</a-button>
      </div>
    </a-drawer>
  </div>
</template>
<script>
// TBD
// filters
// update, create, delete (multi select), export to CSV?
/*
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "address": {
      "street": "Skiles Walks",
      "suite": "Suite 351",
      "city": "Roscoeview",
      "zipcode": "33263",
      "geo": {
        "lat": "-31.8129",
        "lng": "62.5342"
      }
    },
    "phone": "(254)954-1289",
    "website": "demarco.info",
    "company": {
      "name": "Keebler LLC",
      "catchPhrase": "User-centric fault-tolerant solution",
      "bs": "revolutionize end-to-end systems"
    }
  },
*/

import { reactive, ref, computed, watch, onMounted } from 'vue'

export default {
  setup() {
    // table information
    const table = reactive({
      scroll: { x: 1800, y: 240 },
      pagination: { pageSize: 8, total: 0, current: 1 },
      sorter: null, // single sort only
      filters: [],
      page: 1, // start at page 1
      limit: 8, // 8 records per page
      data: [],
      loading: false,
      columns: [
        { title: 'ID', dataIndex: 'id', width: 80, fixed: 'left', slots: { customRender: 'action' }, },
        { title: 'Name', dataIndex: 'name', filter: true },
        { title: 'Username', dataIndex: 'username', width: 120, sorter: true, filter: true },
        { title: 'E-mail', dataIndex: 'email', sorter: true },
        { title: 'Address', dataIndex: 'address', filter: true },
        { title: 'Latitude', dataIndex: 'lat', width: 100 },
        { title: 'Longitude', dataIndex: 'lng', width: 120 },
        { title: 'Phone', dataIndex: 'phone', width: 150 },
        { title: 'Website', dataIndex: 'website' },
        { title: 'Company', dataIndex: 'company' },
        { title: 'Focus', dataIndex: 'bs' },
      ]
    })

    const filter = reactive({
      visible: false,
      form: {
        name: '',
        owner: '',
        type: '',
        approver: '',
        dateTime: '',
        description: '',
      },
      rules: {
        name: [ { required: true, message: 'Please enter user name', }, ],
        owner: [ { required: true, message: 'Please select an owner', }, ],
        type: [ { required: true, message: 'Please choose the type', }, ],
        approver: [ { required: true, message: 'Please choose the approver', }, ],
        dateTime: [ { required: true, message: 'Please choose the dateTime', type: 'object', }, ],
        description: [ { required: true, message: 'Please enter url description', }, ],
      }

    })
    const filterOpen = () => filter.visible = true
    const filterClose = () => filter.visible = false
    const filterApply = () => filter.visible = false

    const rowSelection = reactive({
      selectedRowKeys: [],
      // Check here to configure the default column
      onChange: selectedRowKeys => {
        console.log('selectedRowKeys changed: ', selectedRowKeys);
        rowSelection.selectedRowKeys = selectedRowKeys;
      }
    })
    // const hasSelected = computed(() => state.selectedRowKeys.length > 0);

    const flatten = (_in) => {
      const out = {
        id: _in.id,
        name: _in.name,
        username: _in.username,
        email: _in.email,
        address: `${_in.address.suite} ${_in.address.street} ${_in.address.city} ${_in.address.zipcode}`,
        lat: _in.address.geo.lat,
        lng: _in.address.geo.lng,
        phone: _in.phone,
        website: _in.website,
        company: _in.company.name,
        bs: _in.company.bs,
      }
      return out
    }

    const find = async () => {
      if (table.loading) return
      table.loading = true
      try {
        const { field = null, order = null } = table.sorter || {}
        // console.log('table.sorter', field, order)
        // sorter field=, order=descend / ascend
        let url = `https://jsonplaceholder.typicode.com/users?_page=${table.pagination.current}&_limit=${table.pagination.pageSize}`
        if (field && order) {
          url += `&_sort=${field}&_order=${order === 'ascend' ? 'asc' : 'desc'}`
        }
        const res = await fetch(url)
        const json = await res.json()
        console.log(json)
        table.data = json.map(item => flatten(item))
        table.pagination.total = 10 // currently has up to 10 records
      } catch (e) {
        alert('Error find' + e.toString())        
      }
      table.loading = false
    }

    const findOne = async (id) => {
      if (table.loading) return
      table.loading = true
      try {
        const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        const json = await res.json()
        const data = flatten(json)
        console.log(data)
      } catch (e) {
        alert('Error findOne' + e.toString())        
      }
      table.loading = false
    }

    const clickId = (item) => {
      alert('See console.log for output')
      console.log('clickId', item)
    }

    onMounted(async () => {
      await find()
    })

    const handleTableChange = (pagination, filters, sorter) => {
      console.log('handleTableChange', pagination, filters, sorter)
      table.pagination = { ...pagination }
      table.sorter = { ...sorter }
      // use our own filters instead
      find()
    }

    const customRow = (record) => {
      return {
        // xxx, // props
        onClick: (event) => console.log('onClick', event, record), // click row
        // onDblclick: (event) => {}, // double click row
        // onContextmenu: (event) => {}  // right button click row
        // onMouseenter: (event) => {}   // mouse enter row
        // onMouseleave: (event) => {}   // mouse leave row
      }
    }
    const customHeaderRow = (column) => {
      return {
        // onClick: () => console.log(column), // click header row
      }
    }

    return {
      table,
      handleTableChange,
      clickId,
      customRow,
      customHeaderRow,

      filter,
      filterOpen,
      filterClose,
      filterApply,

      rowSelection,
    }
  },
}
</script>

<style scoped>
.table-operations {
  margin-bottom: 16px;
}

.table-operations > button {
  margin-right: 8px;
}
</style>