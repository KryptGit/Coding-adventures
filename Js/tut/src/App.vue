<template>
  <h1>My first vue repl app</h1>
  <Modal></Modal>
</template>

<script>
import Modal from './components/modal.vue'

export default {
  name: 'App',
  components: {
    Modal
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
