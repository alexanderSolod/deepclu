<template>
  <div id="app">
    <v-container class="mx-5 my-5">
      <v-card outlined>
        <v-row justify="center" align="center">
          <v-img :src="require('@/assets/logo.png')" max-height="150" contain></v-img>
        </v-row>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header class="font-weight-bold">Info</v-expansion-panel-header>
            <v-expansion-panel-content class="text-body-1">
              Deep-Clu is an application to help you interpret the results of cluster analysis through the use of large language models (LLMs) such as from GPT-4. <br> <br>
              The application enables you to enter the members of clusters and their comparative risks, and the expertise required to interpret them (e.g., Clinical Expert).
              Deep-Clu will use this information to automatically generate an engineered prompt which solicits interpretations from a LLM for each cluster related to labels, mechanisms for co-occurrence and risk for adverse outcomes, and interventions to reduce the risk of those outcomes.
              <br><br>You can review and modify the generated prompt from Deep-Clu, and submit it to GPT-3.5 turbo for interpretation.
            </v-expansion-panel-content>
          </v-expansion-panel>
          
        </v-expansion-panels>
        <v-row justify="center" align="center" class="fill-height">
          <v-col cols="12" sm="4">
            <ClusterForm @form-submitted="updateFormValues" />
          </v-col>
          <v-col cols="12" sm="4">
            <PromptMaker v-bind="formData" @output-generated="handleOutput" />
          </v-col>
          <v-col cols="12" sm="4">
            <ModelOutput :modelOutput="modelOutput" />
          </v-col>
        </v-row>
      </v-card>
    </v-container>

    <footer class="footer">
      <p>Created by Alexander Solod. This software is licensed under the <a href="https://opensource.org/licenses/MIT">MIT Open Source License</a>.</p>
    </footer>
  </div>
</template>

<script>
import ClusterForm from './components/ClusterForm.vue';
import PromptMaker from './components/PromptMaker.vue';
import ModelOutput from './components/ModelOutput.vue';

export default {
  name: 'App',
  components: {
    ClusterForm,
    PromptMaker,
    ModelOutput,
  },
  data() {
    return {
      formData: {
        cluster: '',
        expert: '',
        risk: '',
        questions: '',
      },
      modelOutput: '',
    };
  },
  methods: {
    updateFormValues(payload) {
      this.formData = payload;
    },
    handleOutput(output) {
      this.modelOutput = output;
    },
  },
};
</script>



<style>
#app {
  font-family: 'Roboto', sans-serif;
}


.footer {
  width: 100%;
  padding: 20px;
  text-align: center;
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: #f8f9fa; 
  color: #212529;  
}

</style>