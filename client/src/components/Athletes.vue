<template>
  <div class="container">
      <span v-if="showLoading">
          <vue-loading type="bars" color="#d9544e"
          :size="{ width: '50px', height: '50px' }">
          </vue-loading>
          </span>
      <b-table striped small bordered hover :items="athletes" :fields="fields"></b-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      athletes: [],
      fields: [],
      showLoading: true,
    };
  },
  methods: {
    getAthletes() {
      const path = 'http://localhost:5000/athletes';
      axios.get(path)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res.data)
          this.athletes = res.data.athletes;
          this.fields = res.data.fields;
          this.showLoading = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.showLoading = false;
        });
    },
  },
  created() {
    this.getAthletes();
  },
};
</script>
