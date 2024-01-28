// import React from "react";
import React from "react";
import {
  Create,
  CreateProps,
  Datagrid,
  Edit,
  EditProps,
  List,
  SimpleForm,
  TextField,
  TextInput,
} from "react-admin";

export const UserList = () => (
  <List>
    <Datagrid>
      <TextField source="UserCode" />
      <TextField source="sex" />
      <TextField source="pincode" />
      <TextField source="state" />
      <TextField source="dist_name" />
      {/* <EditButton basePath="/users" />
      <DeleteButton basePath="/users" /> */}
    </Datagrid>
  </List>
);

const UserEdit: React.FC<EditProps> = (props) => (
  <Edit {...props} title={"Edit"}>
    <SimpleForm>
      <TextInput disabled source="UserCode" />
      <TextInput source="sex" />
      <TextInput source="pincode" />
      <TextInput source="state" />
      <TextInput source="dist_name" />
    </SimpleForm>
  </Edit>
);

export const UserCreate: React.FC<CreateProps> = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="id" />
      <TextInput source="sex" />
      <TextInput source="pincode" />
      <TextInput source="state" />
      <TextInput source="dist_name" />
    </SimpleForm>
  </Create>
);

export default UserEdit;
