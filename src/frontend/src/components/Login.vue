<template>
  <b-container id="login">
    <b-row align-h="center">
      <b-col cols="4">
        <b-alert
          v-for="(error, index) in errors"
          :key="index"
          :show="showError"
          dismissible
          variant="danger"
        >
          {{ error }}
        </b-alert>
        <b-form @submit.prevent="onSubmit">
          <b-form-group
            id="input-group-1"
            label="Username:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.username"
              required
              placeholder="Enter username"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Password:"
            label-for="input-2"
          >
            <b-form-input
              id="input-2"
              v-model="form.password"
              type="password"
              required
              placeholder="Enter password"
            ></b-form-input>
          </b-form-group>

          <b-button block type="submit" variant="primary">Login</b-button>
        </b-form>

      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      showError: false,
      errors: []
    }
  },
  methods: {
    onSubmit() {
      this.showError = false
      this.errors = []

      axios.post(
        'http://localhost:8000/login/',
        {
          username: this.form.username,
          password: this.form.password,
        }
      ).then(response => {
        localStorage.auth = response.data.token
        this.$router.push({name: 'dashboard'})
      }).catch(error => {
        this.showError = true
        this.errors = error.response.data.non_field_errors
        this.form.password = ''
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#login {
    margin-top: 60px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
