<template>
  <div ref="gantt"></div>
</template>

<script>
import 'dhtmlx-gantt';

export default{
  name: 'gantt',
  props: {
    tasks: {
      type: Object,
      default() {
        return { data: [], links: [] };
      },
    },
  },

  mounted() {
    // eslint-disable-next-line
    gantt.init(this.$refs.gantt);
    // eslint-disable-next-line
    gantt.parse(this.$props.tasks);
  },
};
</script>
<style>
    @import "../assets/dhtmlxgantt.css";
</style>
