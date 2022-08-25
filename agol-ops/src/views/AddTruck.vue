<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Truck</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Registration</label>
            <div class="control">
              <input
                type="text"
                name="registration"
                class="input"
                v-model="registration"
              />
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
import axios from "axios";
export default {
  name: "AddDriver",
  data() {
    return {
      registration: "",
    };
  },
  methods: {
    async submitForm() {
      // this.$store.commit('setIsLoading', true)
      console.log("Submit Form");
      console.log(this.registration);
      // let config = {
      //   headers: {
      //   "Authorization": localStorage.getItem('Token '+'access_token') ,
      //   }
      //   }
      //   console.log(config);

      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      const registration = { registration: this.registration };

      await axios
        .post("/customer-truck/", registration, config)
        .then((response) => {
          console.log(response.data);
          //  toast({
          //     message: 'The Lead is Added',
          //     type: 'is-success',
          //     dismissible: true,
          //     pauseOnHover: true,
          //     duration: 2000,
          //     position: 'bottom-right',
          // })

          // this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });

      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script>
