pragma solidity ^0.5.1;

import "browser/TradeableERC721Token.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/ownership/Ownable.sol";

/**
 * @title Creature _proxyRegistryAddress (rinkeby) :0xf57b2c51ded3a29e6891aba85459d600256cf317; (mainnet): 0xa5409ec958c83c3f309868babaca7c86dcb077c1
 * Creature - a contract for my non-fungible creatures.
 */
contract Aicryptoart is TradeableERC721Token {
  constructor(address _proxyRegistryAddress) TradeableERC721Token("Aicryptoart", "AICRYP", _proxyRegistryAddress) public {  }

  function baseTokenURI() public view returns (string memory) {
    return "https://aicryptoart-pyapp.herokuapp.com/api/artpiece/";
  }
}