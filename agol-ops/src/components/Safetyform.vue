<script>
import axios from 'axios'
import useSafetyForm from "../resources/composables/trucks";
import {onMounted} from "vue";

export default {
setup() {
  const { truck, trailer, truckid, trailerid, orderid, questions, getTruck, getQuestions } = useSafetyForm()
  
  onMounted(getTruck(), getQuestions())

  return {
    truckid,
    trailerid,
    orderid,
    truck,
    trailer,
    questions
    
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
            questions: this.questions,
            truck: this.truckid,
            trailer: this.trailerid
            
          };
          console.log(payload)
          await axios
          .post(`/checklistcreate/`, payload)
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
    <h3>Safety Inspection</h3>
    
    <div  v-for="question in questions"
                            v-bind:key="question.id">
      <p>{{question.question_desc}}</p>
      <input type="radio" :id="question.id" value="Yes" :name="question.id" v-model="question.value" >
      <label for="yes">Yes</label>
      <br>
      <input type="radio" :id="question.id" value="No" :name="question.id" v-model="question.value" :checked="question.value='No'" >
      <label for="no">No</label>
    </div>
    
    <button type="submit">Submit</button>
  </form>
</template>