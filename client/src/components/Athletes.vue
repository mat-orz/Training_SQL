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
      <b-table striped small bordered hover :items="athletes" :fields="fields"
                      v-if="showAthletesTable">
        <template slot="actions" slot-scope="data">
          <b-btn variant="primary" size='sm'
           @click="selectedAthlete(data.item)">
           Select {{ data.item.A_N }} {{ data.item.A_S }}
           </b-btn>
        </template>
      </b-table>
        <b-btn variant="primary" size='sm' v-if="showSelectedAthlete"
           @click="cancelledAthlete(data.item.A_ID)">Cancel {{ data.item.A_N }} {{ data.item.A_S }}
           </b-btn>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      athletes: [],
      athlete: {},
      fields: [],
      error: '',
      showLoading: true,
      showAthletesTable: false,
      showSelectedAthlete: false,
      athleteId: '',
      atheleteSurname: '',
      atheleteName: '',
    };
  },
  methods: {
    selectedAthlete(data) {
      this.athleteId = data.A_ID;
      this.athleteName = data.A_N;
      this.atheleteSurname = data.A_S;
      this.showSelectedAthlete = true;
      this.showAthletesTable = false;
    },
    cancelledAthlete(whatever) {
      this.athleteId = whatever;
      this.showSelectedAthlete = false;
      this.showAthletesTable = true;
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
          this.showAthletesTable = true;
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
