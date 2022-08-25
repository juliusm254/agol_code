<script>
import axios from 'axios'
import useSafetyForm from "../resources/composables/trucks";
import {onMounted} from "vue";

export default {
setup() {
  const { truck, trailer, truckid, trailerid, truck_pressure, oxygen_content, methane_content, orderid, getTruck } = useSafetyForm()
  
  onMounted(getTruck())

  return {
    truckid,
    trailerid,
    orderid,
    truck,
    trailer,
    truck_pressure,
    oxygen_content,
    methane_content


    
  }
},
data() {
            return {
              // questions:[{question: '', value:''}]
            }
},
methods: {
      async submitForm() {
         
          let config = {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "http://localhost:8000/",
            },
          };

          const payload = {
            order: this.orderid,
            truck: this.truckid,
            trailer: this.trailerid,
            truck_pressure: this.truck_pressure,
            oxygen_content: this.oxygen_content,
            methane_content: this.methane_content

            
          };
          console.log(payload)
          await axios
          .post(`/lab-details/`, payload)
          .then((response) => {
            console.log(response.data)
          })
    },
            
  }
}

</script>

<template>
    <div>
    <h4>Truck Reg: {{ truck }} </h4>
    <h4>Trailer Reg: {{ trailer }} </h4>
    </div>
  <form @submit.prevent="submitForm">
    <h3>Lab Details</h3>
    
    <div class="field">
        <label>Truck Pressure</label>
        <div class="control">
            <input type="number" name="truck_pressure" class="input" v-model="truck_pressure">
        </div>
    </div>

    <div class="field">
        <label>Oxygen content % Volume</label>
        <div class="control">
            <input type="number" name="oxygen_content" class="input" v-model="oxygen_content">
        </div>
    </div>

    <div class="field">
        <label>Methane content % Volume</label>
        <div class="control">
            <input type="number" name="methane_content" class="input" v-model="methane_content">
        </div>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>


