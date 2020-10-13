import Web3 from "web3";

import { HttpProvider } from "web3-core";
import { getFakeTokens } from "./getFakeTokens";

async function getProductionTokens() {
  return []; //
}

export async function getSupportedTokens(web3: Web3) {
  const provider = web3.eth.currentProvider as HttpProvider;
  const host = provider.host;

  const isLocalBlockChain =
    host.indexOf("localhost") !== -1 || process?.env?.NODE_ENV === "production";

  const fetcher = isLocalBlockChain ? getFakeTokens : getProductionTokens;

  const supportedTokens = await fetcher();

  return supportedTokens;
}
