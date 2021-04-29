<template>
  <a-table
    :scroll="table.scroll"
    :columns="table.columns" :data-source="table.dataSource" @change="onChange" rowKey="id"
  >
    <template #filterDropdown="{ setSelectedKeys, selectedKeys, confirm, clearFilters, column }">
      <div style="padding: 8px">
        <a-input
          ref="searchInput"
          :placeholder="`Search ${column.dataIndex}`"
          :value="selectedKeys[0]"
          style="width: 188px; margin-bottom: 8px; display: block"
          @change="e => setSelectedKeys(e.target.value ? [e.target.value] : [])"
          @pressEnter="handleSearch(selectedKeys, confirm, column.dataIndex)"
        />
        <a-button
          type="primary"
          size="small"
          style="width: 90px; margin-right: 8px"
          @click="handleSearch(selectedKeys, confirm, column.dataIndex)"
        >
          <template #icon><SearchOutlined /></template>
          Search
        </a-button>
        <a-button size="small" style="width: 90px" @click="handleReset(clearFilters)">
          Reset
        </a-button>
      </div>
    </template>
    <template #filterIcon="filtered">
      <search-outlined :style="{ color: filtered ? '#108ee9' : undefined }" />
    </template>
    <template #customRender="{ text, column }">
      <span v-if="searchText && searchedColumn === column.dataIndex">
        <template
          v-for="(fragment, i) in text
            .toString()
            .split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))"
        >
          <mark
            v-if="fragment.toLowerCase() === searchText.toLowerCase()"
            class="highlight"
            :key="i"
          >
            {{ fragment }}
          </mark>
          <template v-else>{{ fragment }}</template>
        </template>
      </span>
      <template v-else>
        {{ text }}
      </template>
    </template>
  </a-table>
</template>
<script>
import { defineComponent, onMounted, reactive, ref } from 'vue';
import { SearchOutlined } from '@ant-design/icons-vue';

export default defineComponent({
  components: {
    SearchOutlined,
  },
  setup() {
    const state = reactive({
      searchText: '',
      searchedColumn: '',
    })
    const searchInput = ref()

    const slots = { filterDropdown: 'filterDropdown', filterIcon: 'filterIcon', customRender: 'customRender' }
    const onFilterDropdownVisibleChange = visible => visible && setTimeout(() => searchInput.value.focus(), 0)

    const table = reactive({
      scroll: { x: 1200, y: 480 },
      columns: [
        {
          title: 'ID',
          dataIndex: 'id',
          width: 100,
        },
        {
          title: 'User ID',
          dataIndex: 'userId',
          width: 150,
          sorter: (a, b) => a.userId > b.userId,
        },
        {
          title: 'Title',
          dataIndex: 'title',
          sorter: (a, b) => a.title > b.title,
          slots,
          onFilterDropdownVisibleChange,
          onFilter: (value, record) => record.title.toString().toLowerCase().includes(value.toLowerCase()),
        },
        {
          title: 'Body',
          dataIndex: 'body',
          slots,
          onFilterDropdownVisibleChange,
          onFilter: (value, record) => record.body.toString().toLowerCase().includes(value.toLowerCase()),
        },
      ],
      dataSource: []
    })
    onMounted(async () => {
      // {
      //   "userId": 1,
      //   "id": 1,
      //   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      //   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
      // },
      let url = `https://jsonplaceholder.typicode.com/posts`
      const res = await fetch(url)
      const json = await res.json()
      table.dataSource = [...json]
      console.log(json)
    })
    const onChange = (pagination, filters, sorter) => {
      console.log('params', pagination, filters, sorter);
    };

    const handleSearch = (selectedKeys, confirm, dataIndex) => {
      confirm();
      state.searchText = selectedKeys[0];
      state.searchedColumn = dataIndex;
    };

    const handleReset = clearFilters => {
      clearFilters();
      state.searchText = '';
    };

    return {
      table,
      onChange,

      handleSearch,
      handleReset,
      searchText: '',
      searchInput,
      searchedColumn: '',
    };
  },
});
</script>