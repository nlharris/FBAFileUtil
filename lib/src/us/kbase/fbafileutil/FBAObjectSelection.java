
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
 * <p>Original spec-file type: FBAObjectSelection</p>
 * <pre>
 * ****** FBA Result Converters ******
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "fba_name"
})
public class FBAObjectSelection {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("fba_name")
    private String fbaName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public FBAObjectSelection withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("fba_name")
    public String getFbaName() {
        return fbaName;
    }

    @JsonProperty("fba_name")
    public void setFbaName(String fbaName) {
        this.fbaName = fbaName;
    }

    public FBAObjectSelection withFbaName(String fbaName) {
        this.fbaName = fbaName;
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
        return ((((((("FBAObjectSelection"+" [workspaceName=")+ workspaceName)+", fbaName=")+ fbaName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
