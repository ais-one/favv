<template>
  <a-table
    :scroll="table.scroll"
    :columns="table.columns" :data-source="table.dataSource" @change="onChange" rowKey="id"
  />
</template>
<script>
import { defineComponent, onMounted, reactive, ref } from 'vue';

export default defineComponent({
  setup() {
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
          filter: true,
        },
        {
          title: 'Body',
          dataIndex: 'body',
          filter: true,
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

    return {
      table,
      onChange,
    };
  },
});
</script>