<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Scan Order</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Order No.</label>
                        <div class="control">
                            <input type="text" name="company" class="input" v-model="order_no">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">

                            <!-- Step 4 — Creating Custom Events
When developing applications in Vue.js, there will be times when you need to pass 

data up to a parent component via a custom event. Props are read-only data that are 
passed down to a child from the parent, but a custom action via an $emit is the opposite of that. 
To create the most reusable components, it’s best to think of these as functions. 

You pass data down through props (arguments), and emit values back up to the parent 
(a return value).

To emit an event from the child component to the parent, you use the $emit function.
 Before implementing this, this tutorial will guide you through an example to
  demonstrate how this works.

The $emit function accepts two arguments: 
the action name (a string), and the value to pass up to the parent. 
In the following example, when the user clicks on the button, you are 
sending the value CVG to the parent component under the action favoriteAirport: 

                            <button @click="$emit('favoriteAirport', 'CVG')" class="button is-success">Submit</button>
-->
                            <button value="SAFETY" class="button is-success">Submit</button>
                        </div>
                    </div>                  
                </form>
            </div>
        </div> 
    </div>
</template>


<script>
    import axios from 'axios'

    // import { toast } from 'bulma-toast'

    export default {
        name: 'OrderScan',
        data() {
            return {
                status: 'SAFETY',
                order_no: '',
                order: {}
            }
        },
        methods: {
            async submitForm() {
                
                  const order_no = this.order_no
                  const statusdata = JSON.stringify({ 
                    order_status : this.status
                  })
                  console.log(this.status)                 
                  await axios
                  .put(`/scan-order/${order_no}/`, statusdata)
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
                // this.$store.commit('setIsLoading', false)
            },
            
              
              
        } 
    }
</script>