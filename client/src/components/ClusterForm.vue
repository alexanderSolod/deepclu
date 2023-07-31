<template>
  <div class="outlined">
  <v-form ref="form" @submit.prevent="onSubmit">
    <h2 align="center">Input</h2>
      <v-textarea
      v-model="cluster"
      background-color="light-blue"
      clearable
      id="cluster"
      name="cluster"
      label="Enter the name and members for each cluster"
      hint="For example: Cluster-1: x, y, z"
      rows="5"
      class="form-group light-textarea"
      :rules="requiredField"
    ></v-textarea>

    <v-textarea
      v-model="expert"
      clearable
      id="expert"
      name="expert"
      label="Enter the domain expertise required to interpret your clusters"
      hint=" For example: Clinical, Biology, Chemistry..."
      class="form-group light-textarea"
      rows="5"
      
      :rules="requiredField"
    ></v-textarea>

    <v-textarea
      v-model="risk"
      clearable
      id="risk"
      name="risk"
      label="Enter the comparative risk of each cluster"
      hint="For example: Cluster 1 has a higher risk for..."
      class="form-group light-textarea"
      rows="5"
      
    ></v-textarea>

    <v-textarea
      v-model="questions"
      clearable
      id="questions"
      name="questions"
      label="Enter any additional questions you might have"
      hint="For example: why does cluster x have a higher y..."
      class="form-group light-textarea"
      rows="5"
      
    ></v-textarea>

    <v-btn type="submit" color="blue" block class="form-group">
      Generate Prompt
    </v-btn>
  </v-form>
  </div>
</template>


<script>
export default {
name: 'ClusterForm',
data() {
  return {
    cluster: '',
    expert: '',
    risk: '',
    questions: '',
    requiredField: [v => !!v || 'This field is required']
  }
},

methods: {
  onSubmit() {
      if (this.$refs.form.validate()) {
          this.$emit('form-submitted', {
              cluster: this.cluster,
              expert: this.expert,
              risk: this.risk,
              questions: this.questions,
          });
        }
   }
  }
}
</script>


<style scoped>
.outlined {
  border: 1px solid #000; 
  padding: 20px;
  border-radius: 10px; 
}

.light-textarea ::v-deep textarea{
  background-color: #EEEEEE; /* replace with the color you want */
}

</style>
