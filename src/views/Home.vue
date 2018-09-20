<template>
  <div class="home">
    <conLeft/>
    <conMid/>
  </div>
</template>

<script>
import conLeft from '@/components/con-left.vue';
import conMid from '@/components/con-mid.vue';
export default {
    name: 'home',
    components:{
        conLeft,
        conMid
    }
}
</script>
