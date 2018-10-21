<template>
  <div class="container">

      <span v-if="error">
          <b-alert show variant="danger"> {{ error }}</b-alert>
      </span>
      <span v-if="showLoading">
          <vue-loading type="bars" color="#d9544e"
          :size="{ width: '50px', height: '50px' }">
          </vue-loading>
          </span>
      <b-table striped small bordered hover :items="athletes" :fields="fields">
        <template slot="actions" slot-scope="data">
          <b-btn v-b-modal.modal1 variant="primary" size='sm'
           @click="showModal(data.item.A_N)"> {{ data.item.A_N }}
            {{ data.item.A_S }} Modal</b-btn>
        </template>
        <b-modal ref="myModalRef" hide-footer title="WIP">
        <div class="d-block text-center">
          <h3>Hello From My Modal!</h3>
        </div>
        <b-btn class="mt-3" variant="outline-danger" block @click="hideModal">Close Me</b-btn>
      </b-modal>
      </b-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      athletes: [],
      fields: [],
      error: '',
      showLoading: true,
    };
  },
  methods: {
    showModal(test) {
      // eslint-disable-next-line
      console.log(test);
      this.$refs.myModalRef.show();
    },
    hideModal() {
      // eslint-disable-next-line
      console.log(test);
      this.$refs.myModalRef.hide();
    },
    getAthletes() {
      this.error = '';
      const path = 'http://localhost:5000/athletes';
      axios.get(path)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res.data)

          if (res.data.ERROR) {
            this.error = res.data.ERROR;
          }
          this.athletes = res.data.athletes;
          this.fields = res.data.fields;
          this.showLoading = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.error = error;
          this.showLoading = false;
        });
    },
  },
  created() {
    this.getAthletes();
  },
};
</script>
