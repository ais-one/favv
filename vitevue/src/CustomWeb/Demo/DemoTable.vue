<template>
  <div>
  <a-drawer title="Table 2 - Filter & Sort" :width="512" :visible="form.show" :body-style="{ paddingBottom: '80px' }" @close="formClose" placement="left">
    <a-tabs v-model:activeKey="form.tabFormActiveKey">
      <a-tab-pane key="1" tab="Sort">
        <a-form layout="vertical">
          <a-form-item v-for="(col, index) of table2.columns" :key="index">
            <a-switch v-model:checked="form.sorts[index]" /> {{ col.title }}
          </a-form-item>
        </a-form>
      </a-tab-pane>
      <a-tab-pane key="2" tab="Filter">
        <a-form layout="vertical">
          <a-form-item v-for="(col, index) of table2.columns" :key="index">
            <a-switch v-model:checked="form.filters[index]" /> {{ col.title }}
          </a-form-item>
        </a-form>
      </a-tab-pane>
    </a-tabs>
    <!--
    <a-form layout="vertical">
      <a-form-item v-for="(filter, index) of table.filters" :key="index">
        <a-input-group compact>
          <a-select  style="width: 125px;" placeholder="Column" v-model:value="filter.col">
            <a-select-option v-for="col of table.filterCols" :key="col" :value="col">{{col}}</a-select-option>
          </a-select>
          <a-select style="width: 75px;" placeholder="Operation" v-model:value="filter.op">
            <a-select-option v-for="op of table.filterOps" :key="op" :value="op">{{op}}</a-select-option>
          </a-select>
          <a-input style="width: 125px;" placeholder="Value" v-model:value="filter.value" />
          <a-select style="width: 75px;" placeholder="And Or" v-model:value="filter.andOr">
            <a-select-option v-for="andOr of table.filterAndOr" :key="andOr" :value="andOr">{{andOr}}</a-select-option>
          </a-select>
          <a-button type="primary" @click="() => filterDelete(index)"><template #icon><CloseOutlined /></template></a-button>
        </a-input-group>
      </a-form-item>
    </a-form>
    <a-button :disabled="table.filters.length > 9" style="margin-bottom: 8px;" @click="filterAdd">Add Filter</a-button>
    <div
      :style="{
        position: 'absolute', right: 0, bottom: 0, width: '100%', borderTop: '1px solid #e9e9e9', padding: '10px 16px', background: '#fff', textAlign: 'right', zIndex: 1,
      }"
    >
      <a-button type="primary" @click="filterApply">Apply</a-button>
    </div>
    -->
  </a-drawer>
  <a-tabs v-model:activeKey="tabActiveKey">
    <a-tab-pane key="1" tab="Table 1">
      <a-table :scroll="table.scroll" :columns="table.columns" :data-source="table.dataSource" @change="onChange" rowKey="id">
        <template #filterDropdown="{ setSelectedKeys, selectedKeys, confirm, clearFilters, column }">
          <div style="padding: 8px">
            <a-input ref="searchInput" :placeholder="`Search ${column.dataIndex}`" :value="selectedKeys[0]" style="width: 188px; margin-bottom: 8px; display: block"
              @change="e => setSelectedKeys(e.target.value ? [e.target.value] : [])"
              @pressEnter="handleSearch(selectedKeys, confirm, column.dataIndex)"
            />
            <a-button type="primary" size="small" style="width: 90px; margin-right: 8px" @click="handleSearch(selectedKeys, confirm, column.dataIndex)">
              <template #icon><SearchOutlined /></template>Search
            </a-button>
            <a-button size="small" style="width: 90px" @click="handleReset(clearFilters)">Reset</a-button>
          </div>
        </template>
        <template #filterIcon="filtered">
          <search-outlined :style="{ color: filtered ? '#108ee9' : undefined }" />
        </template>
        <template #customRender="{ text, column }">
          <span v-if="searchText && searchedColumn === column.dataIndex">
            <template v-for="(fragment, i) in text.toString().split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))">
              <mark v-if="fragment.toLowerCase() === searchText.toLowerCase()" class="highlight" :key="i">{{ fragment }}</mark>
              <template v-else>{{ fragment }}</template>
            </template>
          </span>
          <template v-else>{{ text }}</template>
        </template>
      </a-table>
    </a-tab-pane>
    <a-tab-pane key="2" tab="Table 2">
      <a-form-item>
        <a-button @click="formOpen">Filter/Sort</a-button>
        <a-button @click="downloadCsv">Export CSV</a-button>
        <a-button @click="copyPaste">Copy CSV</a-button>
        <a-input-group>
          <a-select v-model:value="andOr2" style="width: 40%;">
            <a-select-option value="and">And</a-select-option>
            <a-select-option value="or">Or</a-select-option>
          </a-select>
          <a-input-search placeholder="Search (Seperate by space)" enter-button @search="onSearch2" v-model:value="searchVal2" />
        </a-input-group>
      </a-form-item>
      <a-table :scroll="table2.scroll" :columns="table2.columns" :data-source="table2.filteredData" @change="onChange2" rowKey="id">
        <template #filterDropdown="{ setSelectedKeys, selectedKeys, confirm, clearFilters, column }">
        </template>
        <template #filterIcon="filtered">
          <search-outlined />
        </template>
        <template #customRender="{ text, column }">
          <span v-if="filters2.includes(column.dataIndex)">
            <template v-for="(fragment, i) in text.toString().split(' ')">
              <mark v-if="searchVal2.toLowerCase().split(' ').includes(fragment.toLowerCase())" class="highlight" :key="i">{{ fragment }}</mark>
              <template v-else>{{ fragment }}</template>
            </template>
          </span>
          <template v-else>{{ text }}</template>
        </template>
      </a-table>
    </a-tab-pane>
  </a-tabs>
  </div>
</template>

<script>
import { defineComponent, onMounted, reactive, ref } from 'vue';
import { SearchOutlined } from '@ant-design/icons-vue';
import { downloadData, jsonToCsv } from '~/utils.js'


export default defineComponent({
  components: {
    SearchOutlined,
  },
  setup() {
    // Common Properties And Methods ---------------------------------------------------------------------------------------------------------------------
    const tabActiveKey = ref('2')

    const processTable = (table) => {
      table.columns.forEach(col => {
        const key = col.dataIndex
        if (col.sort) col.sorter = (a, b) => a[key] > b[key]
        else if (col.sorter) delete col.sorter

        if (col.slots) delete col.slots
        if (col.onFilterDropdownVisibleChange) delete col.onFilterDropdownVisibleChange
        if (col.onFilter) delete col.onFilter

        if (col.dropdownFilter) {
          col.slots = { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'customRender' }
          col.onFilterDropdownVisibleChange = visible => visible && setTimeout(() => searchInput.value.focus(), 0)
          col.onFilter = (value, record) => record[key].toString().toLowerCase().includes(value.toLowerCase())
        } else if (col.filter) {
          col.slots = { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'customRender' }
        }
      })
    }

    // Table 1 -------------------------------------------------------------------------------------------------------------------------------------------
    // Table 1 Properties And Methods
    const state = reactive({
      searchText: '',
      searchedColumn: '',
    })
    const searchInput = ref()

    const table = reactive({
      scroll: { x: 1200, y: 480 },
      columns: [
        { title: 'ID', dataIndex: 'id', width: 100 },
        { title: 'User ID', dataIndex: 'userId', width: 150, sort: true },
        { title: 'Title', dataIndex: 'title', sort: true, dropdownFilter: true },
        { title: 'Body', dataIndex: 'body', dropdownFilter: true },
      ],
      dataSource: []
    })
    processTable(table)

    const onChange = (pagination, filters, sorter) => {
      // console.log('params', pagination, filters, sorter)
    }

    const handleSearch = (selectedKeys, confirm, dataIndex) => {
      confirm()
      state.searchText = selectedKeys[0]
      state.searchedColumn = dataIndex
    }

    const handleReset = clearFilters => {
      clearFilters()
      state.searchText = ''
    }

    // Table 2 -------------------------------------------------------------------------------------------------------------------------------------------
    // Table 2 Properties And Methods
    const table2 = reactive({
      scroll: { x: 1200, y: 480 },
      columns: [
        { title: 'ID', dataIndex: 'id', width: 100, sort: true},
        { title: 'User ID', dataIndex: 'userId', width: 150, sort: false, },
        { title: 'Title', dataIndex: 'title', filter: true, slots: { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'customRender' }, sort: false },
        { title: 'Body', dataIndex: 'body', filter: true, slots: { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'customRender' }, sort: false },
      ],
      dataSource: [],
      filteredData: []
    })

    const andOr2 = ref('and')
    const searchVal2 = ref('')
    const filters2 = ref([])
    const form = reactive({
      show: false,
      tabFormActiveKey: '1',
      filters: [],
      sorts: []
    })

    processTable(table2)

    const onChange2 = (pagination, filters, sorter) => {
      // console.log('params2', pagination, filters, sorter)
    }

    const onSearch2 = val => {
      if (!val) return table2.filteredData = [...table2.dataSource]
      const val_a = val.split(' ') // get array of strings to search for

      table2.filteredData = table2.dataSource.filter(row => {
        if (!filters2.value.length) return true
        if (andOr2.value === 'and') {
          return filters2.value.find(col => {
            const rowVal = row[col].toString().toLowerCase()
            return val_a.every(word => rowVal.includes(word.toLowerCase()))
          })
        } else { // or logic
          return filters2.find(col => {
            const rowVal = row[col].toString().toLowerCase()
            return val_a.find(word => rowVal.includes(word.toLowerCase()))
          })
        }
        // row[col].toString().toLowerCase().includes(word.toLowerCase()))
      })
      // console.log(val, table2.filteredData.length)
    }

    const downloadCsv = () => {
      const csv = jsonToCsv(table2.filteredData)
      downloadData(csv, 'test.csv')
    }
    const copyPaste = () => {
      const csv = jsonToCsv(table2.filteredData)
      const el = document.createElement('textarea')
      el.value = csv
      document.body.appendChild(el)
      el.select()
      document.execCommand('copy')
      document.body.removeChild(el)
    }

    const formOpen = () => {
      form.filters = []
      form.sorts = []
      table2.columns.forEach((col, idx) => {
        form.filters.push(col.filter)
        form.sorts.push(col.sort)
      })
      form.show = true
    }
    const formClose = () => {
      table2.columns.forEach((col, idx) => {
        if (form.filters[idx]) {
          table2.columns[idx].filter = true
        } else {
          table2.columns[idx].filter = false
        }
        if (form.sorts[idx]) {
          table2.columns[idx].sort = true
        } else {
          table2.columns[idx].sort = false
        }
      })
      processTable(table2)
      form.show = false
    }

    // Common Lifecycle Method ---------------------------------------------------------------------------------------------------------------------------
    onMounted(async () => {
      filters2.value = table2.columns.filter(item => item.filter).map(item => item.dataIndex)

      let url = `https://jsonplaceholder.typicode.com/posts`
      const res = await fetch(url)
      const json = await res.json()
      table.dataSource = [...json]
      table2.dataSource = [...json]
      table2.filteredData = [...json]
      // console.log(json)
    })

    return {
      tabActiveKey,

      // table 1
      table,
      onChange,
      handleSearch,
      handleReset,
      searchText: '',
      searchInput,
      searchedColumn: '',

      // table 2
      table2,
      onChange2,
      onSearch2,
      filters2,
      andOr2,
      searchVal2,
      formOpen,
      formClose,
      form,
      downloadCsv,
      copyPaste,
    };
  },
});
</script>