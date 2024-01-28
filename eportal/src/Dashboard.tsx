import {
  Box,
  Card,
  CardContent,
  CardMedia,
  Grid,
  Typography,
} from "@mui/material";

import "./css/marquee.css";

// export const AnimatedFooter = () => (
//   <Box className="footer">
//     <Typography variant="subtitle1" className="footer-text">
//       AI/ML Project by Aryan Dalmia, BE Computer Science, BITS Pilani
//     </Typography>
//   </Box>
// );

export const AnimatedFooter = () => (
  <Box className="footer marquee">
    <Typography variant="subtitle1" className="footer-text marquee-text">
      AI/ML Project by Aryan Dalmia, BE Computer Science, BITS Pilani
    </Typography>
  </Box>
);

export const Dashboard = () => (
  <>
    <Typography variant="h4" align="center">
      Welcome to the Samadhaan
    </Typography>
    <span>&nbsp;</span>
    <Typography variant="h6" align="center">
      Grievance Redressal powered by AI (GoI)
    </Typography>
    {/* <Typography variant="h6" align="center">
      Government Of India
    </Typography> */}
    <span>&nbsp;</span>
    <span>&nbsp;</span>
    <span>&nbsp;</span>
    <Grid container spacing={6} alignContent={"center"}>
      {/* Example Summary Card */}
      <Grid item md={12} alignSelf={"center"}>
        <Card>
          <CardMedia
            component="img"
            alt="Samadhaan"
            height="240"
            image="assets/center-image.png" // Replace with your image URL
          />
          <Grid container spacing={2}>
            {/* First Column */}
            <Grid item xs={12} sm={6}>
              <Card>
                <CardContent>
                  <Typography color="textSecondary">
                    Grievances Received
                  </Typography>
                  <Typography variant="h4">
                    {/* Replace with dynamic data */}
                    1,024
                  </Typography>
                </CardContent>
              </Card>
              <Card>
                <CardContent>
                  <Typography color="textSecondary">
                    Last-Mile Nodal Officer Accuracy
                  </Typography>
                  <Typography variant="h4">80%</Typography>
                </CardContent>
              </Card>
            </Grid>

            {/* Second Column */}
            <Grid item xs={12} sm={6}>
              <Card>
                <CardContent>
                  <Typography color="textSecondary">
                    Grievances Disposed
                  </Typography>
                  <Typography variant="h4">1,021</Typography>
                </CardContent>
              </Card>
              <Card>
                <CardContent>
                  <Typography color="textSecondary">
                    Grievance Enhanced With AI
                  </Typography>
                  <Typography variant="h4">5 Parameters</Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Card>
      </Grid>

      {/* Add more cards here for different metrics */}
    </Grid>
    <AnimatedFooter />
  </>
);
