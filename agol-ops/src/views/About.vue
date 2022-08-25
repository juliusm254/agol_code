<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>                
                               
                <form @submit.prevent="getOrders">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success">Search</button>
                        </div>
                    </div>
                </form>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Company</th>
                            <th>Destination</th>
                            <th>Loaded Qty</th>                            
                            <th>Status</th>
                            <th> Created at</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="order in orders"
                            v-bind:key="order.id">                                
                                <td>{{ order.id }}</td>
                                <td>{{ order.customer }}</td>
                                <td>{{ order.destination }}</td>
                                <td>{{ order.loaded_quantity }}</td>
                                <td>{{ order.status }}</td>
                                <td>{{ order.created_at }}</td>
                               
                        </tr>

                    </tbody>
                </table>

                <div class="buttons">
                    <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Prev</button>
                    <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>
                </div>
            </div>
        </div>              
        
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'About',
        data() {
            return {
                orders: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_orders: 0
            }
        },
        mounted() {
            this.getOrders()
        },
        methods: {
            goToNextPage() {
                this.currentPage += 1
                this.getOrders()
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getOrders()
            },

            async getOrders() {
                // this.$store.commit('setIsLoading', true)
                this.showNextButton = false
                this.showPreviousButton = false

                await axios
                    .get(`/order/`)
                    .then(response => {
                        console.log(response.data)
                        this.orders = response.data
                        this.num_orders = response.data.count
                    })

                // await axios
                //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
                //     .then(response => {
                //         this.leads = response.data.results
                //         console.log(response.data)
                        
                //     // for (let i = 0; i < response.data.length; i++) {
                //     //     this.leads.push(response.data[i]) 

                //         if (response.data.next) {
                //             this.showNextButton = true
                //         }
                //         if (response.data.previous) {
                //             this.showPreviousButton = true
                //         }
                    // })
                
                    .catch(error => {
                        console.log(error)
                    })
                // this.$store.commit('setIsLoading', false)
            }
        }
    }
    
</script>