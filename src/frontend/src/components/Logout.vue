<script>
export default {
  name: 'Logout',
  mounted() {
    localStorage.removeItem('auth')
    this.$router.push({name: 'login'})
  }
}
</script>