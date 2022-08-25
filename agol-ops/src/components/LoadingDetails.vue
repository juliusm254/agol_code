<script>
import axios from 'axios'
import useSafetyForm from "../resources/composables/trucks";
import {onMounted} from "vue";

export default {
setup() {
  const { gross_weight, net_weight, tare_weight, truck, trailer, truckid, trailerid, orderid, getTruck } = useSafetyForm()
  
  onMounted(getTruck())

  return {
    truckid,
    trailerid,
    orderid,
    truck,
    trailer,
    gross_weight,
    net_weight,
    tare_weight


    
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
            gross_weight: this.gross_weight,
            net_weight: this.net_weight,
            tare_weight: this.tare_weight

            
          };
          console.log(payload)
          await axios
          .post(`/loading/`, payload)
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
    <h3>Post Loading Details</h3>
    
    <div class="field">
        <label>Gross Weight</label>
        <div class="control">
            <input type="number" name="gross_weight" class="input" v-model="gross_weight">
        </div>
    </div>

    <div class="field">
        <label>Tare Weight</label>
        <div class="control">
            <input type="number" name="tare_weight" class="input" v-model="tare_weight">
        </div>
    </div>

    <div class="field">
        <label>Net Weight</label>
        <div class="control">
            <input type="number" name="net_weight" class="input" v-model="net_weight">
        </div>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>


