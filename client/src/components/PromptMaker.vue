<template>
  <div class="outlined">
    <h2 align="center">Prompt</h2>
    <div class="test">
    <v-textarea 
      id="finalPrompt" 
      clearable
      rows="24" 
      class="form-group my-textarea" 
      v-model="final_prompt"
    ></v-textarea>
    </div>
    <v-btn color="blue" block class="form-group" @click="generateOutput">
      Interpert Cluster

      <v-progress-circular
      v-if="isLoading"
      indeterminate
      color="white"
      size="20"
      width="2"
    ></v-progress-circular>
    </v-btn>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PromptMaker',
  props: {
    expert: String,
    cluster: String,
    risk: String,
    questions: String,
  },
  data() {
    return {
      final_prompt: "",
      isLoading: false
    };
  },
  watch: {
    expert: 'generatePrompt',
    cluster: 'generatePrompt',
    risk: 'generatePrompt',
    questions: 'generatePrompt',
  },
  methods: {
    generatePrompt() {
      this.final_prompt = `You are an expert in ${this.expert} skilled in providing detailed analysis. You will be given as input a list of 
        clusters each containing a set of co-occurring factors, the comparative risks between pairs of clusters, followed by 
        a list of questions. Please use the input in addition to your own ${this.expert} knowledge for answering the questions as 
        completely as possible, and in an easy-to-read format.
        
        The Clusters include the following:
        ${this.cluster}

        The comparative risk between pairs of clusters includes the following:
        ${this.risk}
        
        Please provide all answers to the following questions for a cluster, before addressing them for the next cluster:
        1. What label would best describe the co-occurring factors in each cluster?
        2. Why do the factors in each cluster co-occur?
        3. What are the potential mechanisms in each cluster?
        4. What other potential risks for adverse outcomes can be predicted for individuals in each cluster?
        5. What interventions could reduce the risk in each cluster?
        Please also answer the following question:
        ${this.questions}
      `;
    },

    async generateOutput() {
      this.isLoading = true;
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/generate', { // Edit this with whatever server information you are using
          prompt: this.final_prompt,
        });
        this.$emit('output-generated', response.data.output);
      } catch (error) {
        console.error(error);
      } finally{
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
.outlined {
  border: 1px solid #000; 
  padding: 21px; 
  border-radius: 10px;
}

.my-textarea ::v-deep textarea {
  background-color: #EEEEEE; 
  color: #000;
}

</style>

