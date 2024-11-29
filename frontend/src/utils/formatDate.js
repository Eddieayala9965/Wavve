import moment from "moment";

export const formatTimestamp = (timestamp) => {
  return moment(timestamp).format("MMM DD, YYYY [at] hh:mm A");
};

export const timeAgo = (timestamp) => {
  return moment(timestamp).fromNow();
};
