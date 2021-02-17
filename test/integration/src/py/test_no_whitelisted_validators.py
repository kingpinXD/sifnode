# This test needs an environment where you have no whitelisted validators.
#
# the ./execute_integration_tests_whitelisted_validators.sh script sets that up and runs this test.

import pytest

import pytest_utilities
import test_utilities
from burn_lock_functions import EthereumToSifchainTransferRequest
from pytest_utilities import generate_minimal_test_account

pytestmark = [pytest.mark.individual_file]


@pytest.mark.usefixtures("no_whitelisted_validators")
def test_transfer_eth_to_ceth_without_a_validator_should_throw_exception(
        basic_transfer_request: EthereumToSifchainTransferRequest,
        source_ethereum_address: str,
):
    with pytest.raises(Exception):
        basic_transfer_request.ethereum_address = source_ethereum_address
        return generate_minimal_test_account(
            base_transfer_request=basic_transfer_request,
            target_ceth_balance=10,
            timeout=5
        )
