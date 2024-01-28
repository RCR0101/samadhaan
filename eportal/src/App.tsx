import BusinessIcon from "@mui/icons-material/Business";
import LiveHelpIcon from "@mui/icons-material/LiveHelp";
import PeopleIcon from "@mui/icons-material/People";
import indigo from "@mui/material/colors/indigo";

import { Admin, Resource, defaultTheme } from "react-admin";
import { Dashboard } from "./Dashboard";
import { ComplaintsList } from "./complaint_list";
import ComplaintResponse from "./complaint_response";
import { ComplaintList } from "./complaints";
import myDataProvider from "./dataProvider";
import UserEdit, { UserCreate, UserList } from "./users";

const lightTheme = defaultTheme;

const darkTheme = { ...defaultTheme, palette: { mode: "dark" } };

const myTheme = {
  palette: {
    primary: indigo,
    contrastThreshold: 3,
    tonalOffset: 0.2,
  },
  typography: {
    // Use the system font instead of the default Roboto font.
    fontFamily: [
      "-apple-system",
      "BlinkMacSystemFont",
      '"Segoe UI"',
      "Arial",
      "sans-serif",
    ].join(","),
  },
};

export const App = () => (
  <Admin dataProvider={myDataProvider} dashboard={Dashboard} theme={darkTheme}>
    <Resource
      name="Complaints"
      list={ComplaintList}
      edit={ComplaintResponse}
      // create={ComplaintEdit}
      icon={LiveHelpIcon}
    />
    <Resource
      name="Departments"
      list={ComplaintsList}
      // edit={EditGuesser}
      // show={ShowGuesser}
      icon={BusinessIcon}
    />
    <Resource
      name="Users"
      list={UserList}
      show={UserEdit}
      create={UserCreate}
      icon={PeopleIcon}
      recordRepresentation="name"
    />
    {/* <Resource
      name="posts"
      list={PostList}
      edit={PostEdit}
      create={PostCreate}
      icon={PostIcon}
    />
    <Resource
      name="users"
      list={UserList}
      show={ShowGuesser}
      icon={UserIcon}
      recordRepresentation="name"
    /> */}
  </Admin>
);
