import axios from "axios";

export const sendURL = async (YouTubeURL: any) => {
  const body = JSON.stringify(YouTubeURL);

  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  await axios.post("http://127.0.0.1:5000/converter", body, config);

  const response = window.location.assign("http://127.0.0.1:5000/converter");

  //const response = await getFile();

  //const response = window.location.assign("http://127.0.0.1:5000/converter");
  //return response;
};

export const getFile = async () => {
  const response = window.location.assign("http://127.0.0.1:5000/getFile");
  console.log(response);

  return response;
};
