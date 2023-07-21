<template>
  <div>
    <v-container>
      <UserProfile />
    </v-container>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import UserProfile from "../components/UserProfile.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    UserProfile,
  },
});
</script>
