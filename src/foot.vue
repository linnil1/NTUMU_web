<template>
  <footer class="footer">
    <div class="container">
      <p>Author : linnil1 (楊氏廣法太極拳社)</p>
      <p>PowerBy :
        <a href="http://vuejs.org/" target="_blank">Vuejs</a>,
        <a href="http://getbootstrap.com/" target="_blank">Bootstrap</a>
      </p>
      <p><a href="https://github.com/linnil1/NTUMU_web" target="_blank">Star me on Github </a></p>
    </div>
  </footer>
</template>

<script>

export default {
  name: 'foot'
};
</script>

<style scoped>
.footer {
  background-color:  #5f5f5f;
  bottom: 0;
  width: 100%;
}
.footer *{
  text-align: center;
  color: white !important;
}

</style>
