<template>
  <form @submit.prevent="submitForm">
    <h3>Add a New Book</h3>

    <div>
      <p>1. Is you with us?</p>
      <input type="radio" id="yes" value="True" v-model="q1">
      <label for="yes">Yes</label>
      <br>
      <input type="radio" id="no" value="False" v-model="q1">
      <label for="no">No</label>
    </div>

    <div>
      <p>1. Is you with them?</p>
      <input type="radio" id="yes" value="True" v-model="q2">
      <label for="yes">Yes</label>
      <br>
      <input type="radio" id="no" value="False" v-model="q2">
      <label for="no">No</label>
    </div>

    

    
    <button value="Safety">Add Book</button>
  </form>
</template>

<script>
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
              order:{},
                q1: 'False',
                q2: 'False',
                q3: 'False',
                status: 'Safety'
            }
        },
        // Getting note from backend
      // mounted() {
      //     this.getOrder()                         
      //     },
      
      methods: {

          async getOrder(){
          // this.$store.commit('setIsLoading', true)
              
          const order_no = this.$route.params.id
          
          
          await axios
              .get(`/operations/checklist/${order_no}/`)
              .then(response => {
                  this.order = response.data
              })
              .catch(error => {
                  console.log(error)
              })

              // this.$store.commit('setIsLoading', false)

          },          
          async submitForm() {
                
                  const order_no = this.$route.params.id
                  const formdata = JSON.stringify({
                    status : this.status,
                    q1 : this.q1,
                    q2 : this.q2,
                    q3 : this.q3
                })
                  console.log(this.order.status)                 
                  await axios
                  .post(`/operations/checklist/${order_no}/`, formdata )
                  .then(response => {
                        //  toast({
                        //     message: 'The Lead is Added',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        console.log(response.data)
                        // this.order = (response.data)
                        // console.log(this.order)
                        // this.$router.push('/dashboard/leads/')
                    })
                    .catch(error => {
                        
                        console.log(error)
                    })
                  const statusdata = JSON.stringify({ 
                    status : this.status
                  })
                  await axios
                  .put(`/operations/order/${order_no}/`, statusdata)
                  .then(response => {
                        //  toast({
                        //     message: 'The Lead is Added',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        console.log(response.data)
                        // this.order = (response.data)
                        // console.log(this.order)
                        // this.$router.push('/dashboard/leads/')
                    })    
                // this.$store.commit('setIsLoading', false)
            },
  }
}
</script>

<style>
form {
  padding: 10px;
  margin-top: 10px;
  border: 1px dashed #c3c8ce;
}
</style>