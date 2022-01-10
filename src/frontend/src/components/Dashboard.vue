<template>
  <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand :to="{name: 'dashboard'}">Nessus Parser</b-navbar-brand>
    <b-collapse id="nav-collapse" is-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item :to="{name: 'logout'}">Logout</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <br>
  <uploadButton/>
  <br><br><br>
  <fileButtons/>
  </div>
</template>


<script>
import uploadButton from './upload'
import fileButtons from './fileButtons'

export default {
  name: 'Dashboard',
  components: {
    uploadButton,
    fileButtons
  }, 
  methods: {
    }
}


</script>

<style scoped>
</style>
