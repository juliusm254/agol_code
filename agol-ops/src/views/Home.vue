<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Order</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Company</label>
                        <div class="control">
                            <input type="text" name="company" class="input" v-model="company">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact Person</label>
                        <div class="control">
                            <input type="text" class="input" v-model="contact_person">
                        </div>
                    </div>

                    <div class="field">
                        <label>Truck</label>
                        <div class="control">
                            <input type="text" class="input" v-model="truck">
                        </div>
                    </div>

                    <div class="field">
                        <label>Trailer</label>
                        <div class="control">
                            <input type="text" class="input" v-model="trailer">
                        </div>
                    </div>

                    <div class="field">
                        <label>Quantity</label>
                        <div class="control">
                            <input type="text" class="input" v-model="quantity">
                        </div>
                    </div>

                    <div class="field">
                        <label>Destination</label>
                        <div class="control">
                            <input type="text" class="input" v-model="destination">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
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
        name: 'Home',
        data() {
            return {
                company: '',
                contact_person: '',
                truck: '',
                quantity: '',
                trailer: '',
                destination: ''
            }
        },
        methods: {
            async submitForm() {
                // this.$store.commit('setIsLoading', true)
                console.log('Submit Form')
                const order = {
                    company: this.company,
                    contact_person: this.contact_person,
                    truck: this.truck,
                    trailer: this.trailer,
                    quantity: this.quantity,
                    destination: this.destination,

                }
                console.log(order)
                await axios
                    .post('/customers/order/', order)
                    .then(response => {
                        //  toast({
                        //     message: 'The Lead is Added',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })

                        this.$router.push('/dashboard/leads/')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                // this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>