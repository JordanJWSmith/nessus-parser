<template>
	<div class="container">
		<div>
			<h2>Upload Nessus File</h2>
			<hr/>
             <b-alert
                v-for="(error, index) in errors"
                :key="index"
                :show="showError"
                dismissible
                variant="danger"
                >
                {{ error }}
            </b-alert>
			<label>
				<input type="file" name="nessus" @change="handleFileUpload( $event )"/>
			</label>
			<br>
			<b-button v-on:click="submitFile()" :disabled="disableSubmit">Submit</b-button>
            <p v-if="disableSubmit">Please wait. Uploading...</p>
		</div>
	</div>
</template>

<script>
    // Upload function adapted from https://serversideup.net/uploading-files-vuejs-axios/
    
	import axios from 'axios';
	
	export default {
        name: "uploadButton",
		data(){
			return {
				file: '',
                showError: false,
                errors: [],
                disableSubmit: false
			}
		},
		
		methods: {
			handleFileUpload( event ){
				this.file = event.target.files[0];
			},
			
			submitFile(){
                this.showError = false;
                this.errors = [];
                this.disableSubmit = true;
				let formData = new FormData();

                if (!this.file) {
                    this.disableSubmit = false;
                    this.showError = true;
                    this.errors.push('No file selected')
                    return;
                }
				
				formData.append('file', this.file);
				
				axios.post( 'http://localhost:8000/single-file/',
					formData,
					{
						headers: {
								'Content-Type': 'multipart/form-data'
						}
					}
				).then((response) => {
                    this.disableSubmit = false;
                    this.$root.$emit('uploadedFile', response);
                    this.file = '';
				})
				.catch((error) => {
					console.log('failure');
                    console.log('status: ', error.response.status);
                    console.log('response:', error.response.data);
                    this.showError = true;
                    this.errors.push(error.response.data['data']);
                    this.disableSubmit = false;
				});
			}
		}
	}
</script>