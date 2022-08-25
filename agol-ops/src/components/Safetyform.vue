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
            questions: this.questions,
            truck: this.truckid,
            trailer: this.trailerid
            
          };
          console.log(this.orderid)
          await axios
          .post(`/checklist/`, payload)
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
      <!-- <input type="radio" id="yes" value="True" v-model="choice"> -->
      <label for="yes">Yes</label>
      <br>
      <input type="radio" :id="question.id" value="No" :name="question.id" v-model="question.value" >
      <label for="no">No</label>
    </div>
     
    <!-- <div>
      <p>1. Is you with them?</p>
      <input type="radio" id="yes" value="True" v-model="q2">
      <label for="yes">Yes</label>
      <br>
      <input type="radio" id="no" value="False" v-model="q2">
      <label for="no">No</label>
    </div> -->

  
    
    <button type="submit">Add Book</button>
  </form>
</template>

<!-- <script>
import axios from 'axios'
// import { ref } from 'vue'
// import getUser from '../composables/getUser'

// firebase imports
// import { db } from '../firebase/config'
// import { addDoc, collection } from 'firebase/firestore'

export default {
  name:'Safetyform',

      data() {
            return {
              questions:[{question: '', value:''}] ,
              // truck_registration: truck.truck_details['registration'],
              // trailer: {},
              truck: {},
              trailer: {},
              num_orders: ''
                // q2: 'False',
                // q3: 'False',
            }
        },
        // Getting note from backend
      mounted() {
          this.getCheckList()
          // this.getTruckDetails()                        
          },
      computed :{
        async getTruckDetails() {
            this.id = this.$route.params.id;

          await axios
            .get(`/checklist/${this.id}`)
            .then(response => {

// Fix so that we get all truck details including ID

              this.truck = response.data
              this.trailer = response.data
              console.log(response.data)
              return this.truck.length > 0 ? 'Yes' : 'No'
              // this.num_orders = response.data.count
              console.log(JSON.parse(JSON.stringify(response.data)))
            })
            .catch(error => {
                  console.log(error)
              })
          },

      },
      
      methods: {

          async getCheckList(){
          // this.$store.commit('setIsLoading', true)
          
          
          await axios
              .get(`/checklist-questions/`)
              .then(response => {
                console.log(response.data)
                  this.questions = response.data
                  console.log(response.data)
              })
              .catch(error => {
                  console.log(error)
              })

              // this.$store.commit('setIsLoading', false)

          },
          
          async submitForm() {
         
          let config = {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "http://localhost:8000/",
            },
          };

          const payload = {
            order: this.id,
            questions: this.questions,
            truck: 1,
            trailer: 1
            
          };
          console.log(this.id)
          await axios
          .post(`/checklist/`, payload)
          .then((response) => {
            console.log(response.data)
          })
    },
            
  }
}
</script> -->



