<script>
import axios from 'axios'
import useSafetyForm from "../resources/composables/trucks";
import {onMounted} from "vue";

export default {
setup() {
  const { truck, trailer, truckid, trailerid, labResults, orderid, getTruck, getLabResults } = useSafetyForm()

    
  onMounted(getTruck(), getLabResults())

  // const labResultsSelect = ref('')

  const submitForm = async (value) => {
      let config = {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "http://localhost:8000/",
            },
          };

          const payload = {
            status: value.target.value,
            order: orderid.value
            // truck: this.truckid,
            // trailer: this.trailerid,
            // truck_pressure: this.truck_pressure,
            // oxygen_content: this.oxygen_content,
            // methane_content: this.methane_content

            
          };
          console.log(payload)
          await axios
          .post(`/lab-results/`, payload)
          .then((response) => {
            // console.log(response.data)
          })

  }

  return {

    submitForm,
    // labResultsSelect,
    truckid,
    trailerid,
    orderid,
    truck,
    trailer,
    labResults


    
  }
},
data() {
            return {
              // questions:[{question: '', value:''}]
            }
},
}

</script>

<template>
    <div>
    <h4>Truck Reg: {{ truck }} </h4>
    <h4>Trailer Reg: {{ trailer }} </h4>
    </div>
      <h3>Lab Results</h3>

      <h4>Oxygen: {{ labResults.oxygen }}</h4>
      <h4>Pressure: {{ labResults.pressure }}</h4>
      <h4>Nitrogen: {{ labResults.nitrogen }}</h4>
      <h4>Methane: {{ labResults.methane }}</h4>
      <div>
      <button @click="submitForm" type="submit" value="LOADING">Proceed</button>
      </div>
      <div>
      <button @click="submitForm" type="submit" value="REJECT">Reject</button>
      </div>
      
      <button>
        <router-link to="/lab-vent/">Back</router-link>
      </button>
</template>


