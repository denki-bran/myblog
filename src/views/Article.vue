<template>
  <div class="article">
    <conLeft/>
    <conMid/>
  </div>
</template>

<script>
import conLeft from '@/components/con-left.vue';
import conMid from '@/components/con-mid.vue';
export default {
    name: 'article',
    components:{
        conLeft,
        conMid
    }
}
</script>

