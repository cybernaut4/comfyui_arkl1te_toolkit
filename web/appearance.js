import { app } from "../../../scripts/app.js";

app.registerExtension({
  name: "arkl1te_toolkit.appearance",
  nodeCreated(node) {
    switch (node.comfyClass) {
        case "AnythingToString":
            node.setSize([175, 26]);
            node.color = "#312a23";
            node.bgcolor = "#533c31";
            break;
        case "PadZeroes":
            node.setSize([180, 82]);
            node.color = "#312a23";
            node.bgcolor = "#533c31";
        case "Concatenate":
            node.setSize([210, 130]);
            node.color = "#312a23";
            node.bgcolor = "#533c31";
            break;
        case "CountFilesInDirectory":
            node.setSize([210, 82]);
            node.color = "#273233";
            node.bgcolor = "#3d5355";
            break;
    }
  },
  
});