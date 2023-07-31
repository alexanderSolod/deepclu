<template>
  <div class="outlined">
    <h2 align="center">Model Output</h2>
    <div class="scrollable-content">
      <v-textarea
        ref="copyTextarea"
        readonly
        clearable
        rows="24" 
        class="darker-text my-textarea"
        v-model="output"
      ></v-textarea>
    </div>
    <v-btn color="blue" block class="form-group" @click="copyToClipboard">
      Copy to clipboard
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'ModelOutput',
  props: {
    modelOutput: String,
  },
  data() {
    return {
      output: this.modelOutput
    };
  },
  watch: {
    modelOutput(newVal) {
      this.output = newVal;
    },
  },
  methods: {
    copyToClipboard() {
      navigator.clipboard.writeText(this.output).then(() => {
        console.log('Copying to clipboard was successful!');
      }, err => {
        console.error('Could not copy text: ', err);
      });
    },
  },
};
</script>

<style scoped>
.scrollable-content {
  max-height: 715px;
  overflow-y: auto;
}

.outlined {
  border: 1px solid #000;
  padding: 21px;
  border-radius: 10px;
}

.my-textarea ::v-deep textarea {
  background-color: #EEEEEE; /* replace with the color you want */
  color: rgb(212, 8, 8);
}
</style>
