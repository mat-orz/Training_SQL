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
          <b-btn v-b-modal.modal1>Test Modal</b-btn>
      <b-table striped small bordered hover :items="athletes" :fields="fields">
        <template slot="show_details" slot-scope="row">
          <b-btn v-b-modal.myModal>Show Modal</b-btn>
      <!-- we use @click.stop here to prevent emitting of a 'row-clicked' event  -->
      <b-button size="sm" @click.stop="row.toggleDetails" class="mr-2">
       {{ row.detailsShowing ? 'Show' : 'Hide'}} Details
      </b-button>
      <!-- In some circumstances you may need to use @click.native.stop instead -->
      <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
      <b-form-checkbox @click.native.stop @change="row.toggleDetails" v-model="row.detailsShowing">
        Details via check
      </b-form-checkbox>
    </template>
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
          this.showLoading = false;
        });
    },
  },
  created() {
    this.getAthletes();
  },
};
</script>
