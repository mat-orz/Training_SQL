
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
      athlete: {},
      data: [],
    };
  },
  methods: {
    selectedAthlete(data) {
      // eslint-disable-next-line
      console.log(data)
      this.athlete.id = data.A_ID;
      this.athlete.name = data.A_N;
      this.athlete.surname = data.A_S;
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
          this.data = res.data;
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
