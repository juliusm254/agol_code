<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please Sign In</h1>

          <p v-if="incorrectAuth">Incorrect Username</p>
          <form v-on:submit.prevent="login">
          <div class="field">
          <label>Username</label>
            <div class="form-group">
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="input"
              />
            </div>
            </div>
            <div class="field">
            <label>Password</label>
            <div class="form-group">
              
              <input
                type="password"
                name="password"
                id="pass"
                v-model="password"
                class="input"
              />
            </div>
            </div>
            <div class="field">
            <div class="form-group">
              <button type="submit" class="">
                Login
              </button>
            </div>
          </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      type: "OPERATIONS",
      incorrectAuth: false,
    };
  },
  computed: {
    ...mapGetters("auth", {
      loginState: "getLoginState",
    }),
  },
  // created() {
  //     this.actionLogin();
  // },

  methods: {
    ...mapActions("auth", {
      actionLogin: "actionLogin",
    }),

    // ...mapActions(["actionLogin"]),

    async login() {
      console.log(this.username, this.password);

      let config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "http://localhost:8000/",
        },
      };

      const payload = {
        username: this.username,
        password: this.password,
        type: this.type,
      };
      await this.actionLogin(payload, config);
      if (this.loginState == "success") {
        this.$router.push({ name: "Home" });
      } else {
        this.incorrectAuth = true;
      }
    },
  },
};
</script>
