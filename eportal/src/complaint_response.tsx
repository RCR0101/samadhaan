import { DateInput, Edit, EditProps, SimpleForm, TextInput } from "react-admin";

const ComplaintResponse: React.FC<EditProps> = (props) => (
  <Edit {...props} title={"Edit"}>
    <SimpleForm>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
        }}
      >
        <div style={{ flex: 1, marginRight: "1rem" }}>
          {/* Column 1 */}
          {/* Identification Section */}
          <TextInput disabled source="registration_no" />

          {/* Basic Information Section */}
          <TextInput source="title" />
          <DateInput source="DiaryDate.$date" label="Diary Date" />

          {/* Department and User Information */}
          <TextInput source="org_code" />
          <TextInput source="UserCode" />
          {/* <TextInput source="status" /> */}
          <TextInput source="OfficerDetail" />
          <TextInput source="attributes.predicted_dept" label="Department" />
          <TextInput
            source="attributes.predicted_dept_confidence"
            label="Dept Prediction Confidence"
          />
          {/* Attributes Section */}
          <TextInput
            multiline
            source="attributes.severity"
            label="Severity"
            fullWidth
            disabled
          />

          {/* <TextInput source="attributes.severity" label="Severity" disabled /> */}

          {/* Sentiment Section */}
          {/* For ArrayInput, consider if you want it in a single column or split */}
          {/* <ArrayInput source="attributes.sentiment" label="Sentiment" disabled>
            <SimpleFormIterator>
              <TextInput source="label" />
              <NumberInput source="score" />
            </SimpleFormIterator>
          </ArrayInput> */}
        </div>

        <div style={{ flex: 1 }}>
          {/* Column 2 */}
          {/* Fields that are multiline or require full width */}
          <TextInput
            multiline
            source="subject_content_text"
            fullWidth
            disabled
          />

          <TextInput
            multiline
            source="attributes.summary"
            label="Summary"
            fullWidth
            disabled
          />
          <TextInput
            multiline
            source="remarks_text"
            label="Add Response Here"
            fullWidth
          />
          {/* <TextInput
            multiline
            source="attributes.rephrased_text"
            label="Rephrased Text"
            fullWidth
            disabled
          /> */}
        </div>
      </div>
    </SimpleForm>
  </Edit>
);

export default ComplaintResponse;
