<link rel="stylesheet" type="text/css" href="../assets/jsGantt/jsgantt.css" />
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
           @click="cancelledAthlete(athlete.id)">Quit {{ athlete.name }} {{ athlete.surname }}
           </b-btn>
  </div>
</template>

<script src="./Athletes.js"></script>
