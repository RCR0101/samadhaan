import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  ReferenceInput,
  SimpleForm,
  TextField,
  TextInput,
  useRecordContext,
} from "react-admin";

const complaintFilters = [
  <TextInput source="q" label="Search" alwaysOn />,
  <ReferenceInput source="org_code" label="Complaint" reference="complaints" />,
];

export const ComplaintList = () => (
  <List filters={complaintFilters}>
    <Datagrid>
      <TextField source="id" />
      {/* <ReferenceField source="org_code" reference="complaints" link="show" /> */}
      <TextField source="org_code" />
      <TextField source="title" />
      <TextField source="pincode" />

      {/* <RichTextField source="subject_content_text" /> */}
      <EditButton />
    </Datagrid>
  </List>
);

const ComplaintTitle = () => {
  const record = useRecordContext();
  return <span>complaint {record ? `"${record.title}"` : ""}</span>;
};

export const ComplaintEdit = () => (
  <Edit title={<ComplaintTitle />}>
    <SimpleForm>
      <TextInput source="id" disabled />
      <TextField source="pincode" />
      <TextField source="state" />
      {/* <ReferenceInput source="id" reference="complaints" /> */}
      {/* <TextInput source="title" /> */}
      <TextInput
        source="subject_content_text"
        multiline
        rows={5}
        fullWidth
        disabled
      />
      {/* <RichTextField source="subject_content_text" /> */}
      {/* <RichTextField source="remarks_text" multiline rows={5} /> */}
      <TextInput source="remarks_text" multiline rows={5} fullWidth />
      <TextField source="OfficerDetail" />
    </SimpleForm>
  </Edit>
);

export const ComplaintCreate = () => (
  <Create>
    <SimpleForm>
      <ReferenceInput source="id" reference="complaints" />
      <TextInput source="title" />
      <TextInput source="body" multiline rows={5} />
    </SimpleForm>
  </Create>
);
