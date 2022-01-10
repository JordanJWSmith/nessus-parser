<template>
	<div class="container">
		<div>
			<h2>Uploaded Files</h2>
			<hr/>
                <div v-if="fileList.length > 0">
                    <table>
                        <tr>
                            <th>File Name</th>
                            <th></th>
                        </tr>
                        <tr 
                        v-for="(file, index) in fileList"
                        :key="index"
                        >
                            <td>
                                <b-button 
                                :href="'report/'+file.policy_id"
                                variant="info"
                                >
                                {{ file.name }}
                                </b-button>
                            </td>
                            <td >
                                <b-button
                                class="delete-button"
                                variant="danger"
                                :disabled="deleteDisabled"
                                v-on:click="deleteFile(file.policy_id)" 
                                >
                                    Delete 
                                </b-button>
                            </td>
                            
                        </tr>
                    </table>

                </div>
                <div v-else>
                    <p>You have not uploaded any Nessus files</p>
                </div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	
	export default {
        name: "fileButtons",
		data(){
			return {
				fileList: [],
                deleteDisabled: false
			}
		},
		
		methods: {
            getFiles() {
                axios.get('http://localhost:8000/report/')
                .then((response) => {
                    this.fileList = response.data.data
                    this.deleteDisabled = false;
                });
            },
            deleteFile(id) {
                this.deleteDisabled = true;
                axios.delete('http://localhost:8000/delete-all/'+id)
                .then((response) => {
                    console.log(response)
                    this.getFiles();
                })
            }
		},
        beforeMount(){
            this.getFiles()
        },
        mounted() {
            this.$root.$on('uploadedFile', (response) => {
                this.getFiles();
            })
        }
	}
</script>

<style scoped>
.delete-button {
    margin: 30px;
}

th {
    min-width: 10vw;
}

</style>