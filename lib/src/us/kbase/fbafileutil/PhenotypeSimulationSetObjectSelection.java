
package us.kbase.fbafileutil;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: PhenotypeSimulationSetObjectSelection</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "phenotype_simulation_set_name"
})
public class PhenotypeSimulationSetObjectSelection {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("phenotype_simulation_set_name")
    private String phenotypeSimulationSetName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public PhenotypeSimulationSetObjectSelection withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("phenotype_simulation_set_name")
    public String getPhenotypeSimulationSetName() {
        return phenotypeSimulationSetName;
    }

    @JsonProperty("phenotype_simulation_set_name")
    public void setPhenotypeSimulationSetName(String phenotypeSimulationSetName) {
        this.phenotypeSimulationSetName = phenotypeSimulationSetName;
    }

    public PhenotypeSimulationSetObjectSelection withPhenotypeSimulationSetName(String phenotypeSimulationSetName) {
        this.phenotypeSimulationSetName = phenotypeSimulationSetName;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((("PhenotypeSimulationSetObjectSelection"+" [workspaceName=")+ workspaceName)+", phenotypeSimulationSetName=")+ phenotypeSimulationSetName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}