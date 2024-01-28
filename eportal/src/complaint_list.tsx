import * as React from "react";
import { Datagrid, List, ListProps, NumberField, TextField } from "react-admin";

interface ComplaintsListProps extends ListProps {
  // Define any additional props here. For example:
  customProp?: string; // optional custom prop
}

export const ComplaintsList: React.FC<ComplaintsListProps> = (props) => (
  <List {...props}>
    <Datagrid rowClick="edit">
      <TextField source="org_code" label="Organization Code" />
      <TextField source="year" label="Year" />
      <TextField source="state" label="State" />
      <NumberField source="total_complaints" label="Total Complaints" />
      <NumberField source="new_complaints" label="New Complaints" />
      <NumberField
        source="in_process_complaints"
        label="In Process Complaints"
      />
      <NumberField source="resolved_complaints" label="Resolved Complaints" />
      <NumberField source="reopened_complaints" label="Reopened Complaints" />
      <NumberField source="feedback_score" label="Feedback Score" />
    </Datagrid>
  </List>
);
