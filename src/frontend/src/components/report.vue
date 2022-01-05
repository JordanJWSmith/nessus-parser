<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand :to="{name: 'dashboard'}">Dashboard</b-navbar-brand>
            <b-collapse id="nav-collapse" is-nav>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-item :to="{name: 'logout'}">Logout</b-nav-item>
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>

        <div>
            <b-jumbotron :header="report.name" lead="Policy and Report Details">
                <p></p>
            </b-jumbotron>
        </div>

        <div class="container">
            <h1>Policy Details </h1>
            <h2>{{ policy.policy_name }}</h2>
            <p v-if="policy.policy_comments !== 'None'"> {{ policy.policy_comments}} </p>
       
            
             <b-form-radio-group id="policyRadio" label="Choose an option to see Policy Details" button-variant="outline-primary" buttons>
                <b-form-radio v-model="radioSelectPolicy" name="some-radios" value="server" @change="popServerPreferences()">Server Preferences</b-form-radio>
                <b-form-radio v-model="radioSelectPolicy" name="some-radios" value="plugin" @change="popPluginPreferences()">Plugin Preferences</b-form-radio>
                <b-form-radio v-model="radioSelectPolicy" name="some-radios" value="family" @change="popFamilySelection()">Family Selection</b-form-radio>
                <b-form-radio v-model="radioSelectPolicy" name="some-radios" value="individual" @change="popIndividualPluginSelection()">Individual Plugin Selection</b-form-radio>
                <b-form-radio v-if="radioSelectPolicy.length > 0" v-model="radioSelectPolicy" name="some-radios" value="">Hide</b-form-radio>
            </b-form-radio-group>
            <br><br>

            <b-table v-if="radioSelectPolicy == 'server'" striped hover sticky-header="600px" :items="serverPreferencesArr" caption-top>
                <template #table-caption><h3>Server Preferences for {{ policy.policy_name }}</h3></template>
            </b-table>
            <b-table v-if="radioSelectPolicy == 'plugin'" striped hover sticky-header="600px" :items="pluginPreferencesArr" caption-top>
                <template #table-caption><h3>Plugin Preferences for {{ policy.policy_name }}</h3></template>
            </b-table>
            <b-table v-if="radioSelectPolicy == 'family'" striped hover sticky-header="600px" :items="familySelectionArr" caption-top>
                <template #table-caption><h3>Family Selection for {{ policy.policy_name }}</h3></template>
            </b-table>
            <b-table v-if="radioSelectPolicy == 'individual'" striped hover sticky-header="600px" :items="individualPluginSelectionArr" caption-top>
                <template #table-caption><h3>Individual Plugin Preferences for {{ policy.policy_name }}</h3></template>
            </b-table>

        </div>

        <hr>

        <div class="container">
            <br>
            <h1>Report Details </h1>
            <h2>{{ report.name }}</h2>

            <p> Choose a Report Host: </p> 
            <select v-model="selected" @change="hostProperties(selected.id); reportItem(selected.id)">
                <option disabled value="">Please select one</option>
                <option
                    v-for="(host, index) in reportHostsArr"
                    :key="index"
                    :value="host"
                    > 
                    {{ host.name }}
                </option>
            </select>

            <br>
            <br>

            <b-form-radio-group v-if="hostPropertiesArr.length > 0" label="Choose an option to see Report Details" button-variant="outline-primary" buttons>
                <b-form-radio v-model="radioSelectReport" name="some-radios" value="host"  >Report Host Properties</b-form-radio>
                <b-form-radio v-model="radioSelectReport" name="some-radios" value="item" >Report Items</b-form-radio>
                <b-form-radio v-if="radioSelectReport.length > 0" v-model="radioSelectReport" name="some-radios" value="">Hide</b-form-radio>
            </b-form-radio-group>
            <br><br>

               
            <b-table v-if="radioSelectReport == 'host'" striped hover caption-top sticky-header="600px" :items="hostPropertiesArr">
                <template #table-caption> <h3> Report Host Properties: {{selected.name}}</h3></template>
            </b-table>
            
            
            <b-table v-if="radioSelectReport == 'item'" striped hover caption-top sticky-header="600px" :items="reportItemArr">
                <template #cell(details)="data">
                    <b-button v-b-modal.modal-scrollable v-on:click="reportItemProperties(data.item.id)">See Detail</b-button>
                </template>
                <template #table-caption><h3>Report Items: {{selected.name}}</h3></template>
            </b-table>

            <b-modal id="modal-scrollable" scrollable title="Item Detail" size="xl" ok-only>
                <b-table striped hover caption-top sticky-header="600px" :items="reportItemPropertiesArr"></b-table>
            </b-modal>  

        </div>

    </div>
    
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'report',
        data(){
			return {
                path: this.$route.params.id,
                selected: {},
                radioSelectPolicy: "",
                radioSelectReport: "",
                policy: {},
                report: {},
                serverPreferencesArr: [],
                pluginPreferencesArr: [],
                familySelectionArr: [],
                individualPluginSelectionArr: [],
                reportHostsArr: [],
                hostPropertiesArr: [],
                reportItemArr: [],
                reportItemPropertiesArr: [],
			}
		},
        methods: {
            policyDetails(id) {
                axios.get('http://localhost:8000/policy/'+id)
                .then((response) => {
                    console.log('policyDetails: ', response.data.data);
                    this.policy = response.data.data
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            serverPreferences(id) {
                axios.get('http://localhost:8000/server-preferences/'+id)
                .then((response) => {
                    console.log('serverPreferences: ', response.data.data);
                    this.serverPreferencesArr = response.data.data;
                    this.policyDets.server = response.data.data
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            pluginPreferences(id) {
                 axios.get('http://localhost:8000/plugin-preferences/'+id)
                .then((response) => {
                    console.log('pluginPreferences: ', response.data.data);
                    this.pluginPreferencesArr = response.data.data;
                    this.policyDets.plugin = response.data.data
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            familySelection(id) {
                 axios.get('http://localhost:8000/family-selection/'+id)
                .then((response) => {
                    console.log('family-selection: ', response.data.data);
                    this.familySelectionArr = response.data.data;
                    this.policyDets.family = response.data.data
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            individualPluginSelection(id) {
                axios.get('http://localhost:8000/individual-plugin-selection/'+id)
                .then((response) => {
                    console.log('individual-plugin-selection: ', response.data.data);
                    this.individualPluginSelectionArr = response.data.data;
                    this.policyDets.individual = response.data.data
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            reportDetails(id) {
                 axios.get('http://localhost:8000/report/'+id)
                .then((response) => {
                    console.log('report: ', response.data.data);
                    this.report = response.data.data;
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            reportHostDetails(id) {
                 axios.get('http://localhost:8000/report-host/'+id)
                .then((response) => {
                    console.log('reportHost: ', response.data.data);
                    this.reportHostsArr = response.data.data;
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            hostProperties(id) {
                 axios.get('http://localhost:8000/host-properties/'+id)
                .then((response) => {
                    console.log('hostProperties: ', response.data.data);
                    this.hostPropertiesArr = response.data.data;
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            reportItem(id) {
                 axios.get('http://localhost:8000/report-item/'+id)
                .then((response) => {
                    console.log('reportItem: ', response.data.data);
                    response.data.data.forEach(item => {
                        item['details'] = "";
                    })
                    this.reportItemArr = response.data.data;
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            reportItemProperties(id) {
                 axios.get('http://localhost:8000/report-item-properties/'+id)
                .then((response) => {
                    console.log('reportItemProperties: ', response.data.data);
                    this.reportItemPropertiesArr = response.data.data;
                })
                .catch((error) => {
                    console.log('error: ', error)
                })
            },

            popServerPreferences() {
                this.showServerPreferences = !this.showServerPreferences;
                if (this.serverPreferencesArr.length == 0) {
                    this.serverPreferences(this.path)
                    
                }
            },

             popPluginPreferences() {
                this.showPluginPreferences = !this.showPluginPreferences;
                if (this.pluginPreferencesArr.length == 0) {
                    this.pluginPreferences(this.path)
                }
            },

            popFamilySelection() {
                this.showFamilySelection = !this.showFamilySelection;
                if (this.familySelectionArr.length == 0) {
                    this.familySelection(this.path)
                }
            },

            popIndividualPluginSelection() {
                this.showIndividualPluginSelection = !this.showIndividualPluginSelection;
                if (this.individualPluginSelectionArr.length == 0) {
                    this.individualPluginSelection(this.path)
                }
            },

            popReportHosts() {
                this.showReportHosts = !this.showReportHosts;
                if (this.reportHostsArr.length == 0) {
                    this.reportHostDetails(this.path)
                }
            },

            
        },
        beforeMount() {
            this.policyDetails(this.path);
            this.reportDetails(this.path);
            this.reportHostDetails(this.path);
        }
    }
</script>


<style scoped>
#report {
    margin-top: 60px;
}

.container {
    margin-left: 60px;
}

</style>