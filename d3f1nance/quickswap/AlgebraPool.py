from typing import List
from raffaelo.interfaces.contracts.interface import iCBC


class QuickSwapV3AlgebraPoolContract(iCBC):

    _ABI: str = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"bottomTick","type":"int24"},{"indexed":true,"internalType":"int24","name":"topTick","type":"int24"},{"indexed":false,"internalType":"uint128","name":"liquidityAmount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"int24","name":"bottomTick","type":"int24"},{"indexed":true,"internalType":"int24","name":"topTick","type":"int24"},{"indexed":false,"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1","type":"uint128"}],"name":"Collect","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"communityFee0New","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"communityFee1New","type":"uint8"}],"name":"CommunityFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"fee","type":"uint16"}],"name":"Fee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"paid1","type":"uint256"}],"name":"Flash","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"virtualPoolAddress","type":"address"}],"name":"Incentive","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint160","name":"price","type":"uint160"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Initialize","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint32","name":"liquidityCooldown","type":"uint32"}],"name":"LiquidityCooldown","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24","name":"bottomTick","type":"int24"},{"indexed":true,"internalType":"int24","name":"topTick","type":"int24"},{"indexed":false,"internalType":"uint128","name":"liquidityAmount","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"int256","name":"amount0","type":"int256"},{"indexed":false,"internalType":"int256","name":"amount1","type":"int256"},{"indexed":false,"internalType":"uint160","name":"price","type":"uint160"},{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Swap","type":"event"},{"inputs":[],"name":"activeIncentive","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"bottomTick","type":"int24"},{"internalType":"int24","name":"topTick","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"bottomTick","type":"int24"},{"internalType":"int24","name":"topTick","type":"int24"},{"internalType":"uint128","name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested","type":"uint128"}],"name":"collect","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"dataStorageOperator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"flash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int24","name":"bottomTick","type":"int24"},{"internalType":"int24","name":"topTick","type":"int24"}],"name":"getInnerCumulatives","outputs":[{"internalType":"int56","name":"innerTickCumulative","type":"int56"},{"internalType":"uint160","name":"innerSecondsSpentPerLiquidity","type":"uint160"},{"internalType":"uint32","name":"innerSecondsSpent","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32[]","name":"secondsAgos","type":"uint32[]"}],"name":"getTimepoints","outputs":[{"internalType":"int56[]","name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]","name":"secondsPerLiquidityCumulatives","type":"uint160[]"},{"internalType":"uint112[]","name":"volatilityCumulatives","type":"uint112[]"},{"internalType":"uint256[]","name":"volumePerAvgLiquiditys","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"globalState","outputs":[{"internalType":"uint160","name":"price","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint16","name":"fee","type":"uint16"},{"internalType":"uint16","name":"timepointIndex","type":"uint16"},{"internalType":"uint8","name":"communityFeeToken0","type":"uint8"},{"internalType":"uint8","name":"communityFeeToken1","type":"uint8"},{"internalType":"bool","name":"unlocked","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint160","name":"initialPrice","type":"uint160"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidity","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"liquidityCooldown","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxLiquidityPerTick","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"bottomTick","type":"int24"},{"internalType":"int24","name":"topTick","type":"int24"},{"internalType":"uint128","name":"liquidityDesired","type":"uint128"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"uint128","name":"liquidityActual","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"positions","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint32","name":"lastLiquidityAddTimestamp","type":"uint32"},{"internalType":"uint256","name":"innerFeeGrowth0Token","type":"uint256"},{"internalType":"uint256","name":"innerFeeGrowth1Token","type":"uint256"},{"internalType":"uint128","name":"fees0","type":"uint128"},{"internalType":"uint128","name":"fees1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"communityFee0","type":"uint8"},{"internalType":"uint8","name":"communityFee1","type":"uint8"}],"name":"setCommunityFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"virtualPoolAddress","type":"address"}],"name":"setIncentive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"newLiquidityCooldown","type":"uint32"}],"name":"setLiquidityCooldown","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool","name":"zeroToOne","type":"bool"},{"internalType":"int256","name":"amountRequired","type":"int256"},{"internalType":"uint160","name":"limitSqrtPrice","type":"uint160"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool","name":"zeroToOne","type":"bool"},{"internalType":"int256","name":"amountRequired","type":"int256"},{"internalType":"uint160","name":"limitSqrtPrice","type":"uint160"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swapSupportingFeeOnInputTokens","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"int16","name":"","type":"int16"}],"name":"tickTable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24","name":"","type":"int24"}],"name":"ticks","outputs":[{"internalType":"uint128","name":"liquidityTotal","type":"uint128"},{"internalType":"int128","name":"liquidityDelta","type":"int128"},{"internalType":"uint256","name":"outerFeeGrowth0Token","type":"uint256"},{"internalType":"uint256","name":"outerFeeGrowth1Token","type":"uint256"},{"internalType":"int56","name":"outerTickCumulative","type":"int56"},{"internalType":"uint160","name":"outerSecondsPerLiquidity","type":"uint160"},{"internalType":"uint32","name":"outerSecondsSpent","type":"uint32"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"timepoints","outputs":[{"internalType":"bool","name":"initialized","type":"bool"},{"internalType":"uint32","name":"blockTimestamp","type":"uint32"},{"internalType":"int56","name":"tickCumulative","type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityCumulative","type":"uint160"},{"internalType":"uint88","name":"volatilityCumulative","type":"uint88"},{"internalType":"int24","name":"averageTick","type":"int24"},{"internalType":"uint144","name":"volumePerLiquidityCumulative","type":"uint144"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFeeGrowth0Token","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFeeGrowth1Token","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'

    def activeIncentive(self) -> str:
        return self.contract.functions.activeIncentive().call()

    def dataStorageOperator(self) -> str:
        return self.contract.functions.dataStorageOperator().call()

    def factory(self) -> str:
        return self.contract.functions.factory().call()

    def getInnerCumulatives(self, bottomTick: int, topTick: int) -> list:
        return self.contract.functions.getInnerCumulatives(bottomTick, topTick).call()

    def getTimepoints(self, secondsAgos: List[int]) -> list:
        return self.contract.functions.getTimepoints(secondsAgos).call()

    def globalState(self) -> list:
        return self.contract.functions.globalState().call()

    def liquidity(self) -> int:
        return self.contract.functions.liquidity().call()

    def liquidityCooldown(self) -> int:
        return self.contract.functions.liquidityCooldown().call()

    def maxLiquidityPerTick(self) -> int:
        return self.contract.functions.maxLiquidityPerTick().call()

    def positions(self, i: bytes) -> list:
        return self.contract.functions.positions(i).call()

    def tickSpacing(self) -> int:
        return self.contract.functions.tickSpacing().call()

    def tickTable(self, i: int) -> int:
        return self.contract.functions.tickTable(i).call()

    def ticks(self, i: int) -> list:
        return self.contract.functions.ticks(i).call()

    def timepoints(self, i: int) -> list:
        return self.contract.functions.timepoints(i).call()

    def token0(self) -> str:
        return self.contract.functions.token0().call()

    def token1(self) -> str:
        return self.contract.functions.token1().call()

    def totalFeeGrowth0Token(self) -> int:
        return self.contract.functions.totalFeeGrowth0Token().call()

    def totalFeeGrowth1Token(self) -> int:
        return self.contract.functions.totalFeeGrowth1Token().call()
