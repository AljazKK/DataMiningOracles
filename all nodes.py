import requests
import chardet
import idna
from decimal import Decimal
import certifi
import time
import pandas as pd

address = ["0x64FE692be4b42F4Ac9d4617aB824E088350C11C2",
           "0x92b6F8358885Da7BddF32BFC9098830c84443bD8",
           "0xf2887d990170E56ef5157a1444Ca8D379151Db65",
           "0xe6eBF20c0bDbfd4bf854DbaAfE2E693B4dBBbDAA",
           "0x58c69aFF4Df980357034eA98AaD35bbF78cBD849",
           "0x60B2582FB902Dff0B99c7AC30ABC08AaEfEEB309",
           "0x58EB922F60Ae3D7A8b9F6cCbe7ae4F05431f998c",
           "0x3Cc242Ee0804882b28A5b32B721523f90476CF12",
           "0x79C6e11bE1C1ed4D91FbE05D458195A2677F14A5",
           "0xFa3Bf60E209abc278BB8980e1B0be59Ae29381f3",
           "0x688E8432e12620474d53b4A26Eb2E84eBEd4245c",
           "0xd2f84264D43635476cd304c5937b8865090676d7",
           "0x4a1803F29fE5350e9A164D9865576Af798e8EeF8",
           "0x98ceEe4047b380A2693377dF431Da1b5bcd48f91",
           "0x0aE3a0E0e3feB67eC83f423B3B653051aa9Bf4D3",
           "0x7175980f1Fd428cDaC792B18a30731DD0c692987",
           "0x74e6ADae80d37b7558772C1B9FC7CC17B918Ddf7",
           "0x3Af6775460372d15Ed0473716CdF5A7677E5Cfd1",
           "0xb25FCb293571ba083bc33dA71159ed2a39A051A1",
           "0xc1D750678cCeDE3E794EE092cD4c913C40935360",
           "0xD6789a87853A77D9aE2AaddcEDFbEc3c42ecBC97",
           "0x575416B26E6e6f548FD4008Cf21875F90F64eEB0", #stocksd.app
           "0xA83533Bc0fa940c46e8371b51799f9800F641da0",
           "0x5b4247e58fe5a54A116e4A3BE32b31BE7030C8A3",
           "0x20A859058D4ae68301003B981D5D675795c64a70",
           "0xe20810F1676f1e1f5A9bbDc519A0d96451847a8A",
           "0x3A8B67C0d153D1F8F931E610C5C79A7Ee51BDe3F",
           "0xB92ec7D213a28e21b426D79EDe3c9BBcf6917c09",
           "0xAEc4eBB0abc0E3977b778cdEFea0B90FAb6836B2",
           "0x5970A45008b4877ba1f09bf655F9223BDEa2B555", #speedy link
           "0x7e94A8A23687D8C7058Ba5625dB2Ce358bCbd244",
           "0x7783BDF43e0858Df08F74c8A7a9FC6b54f1a8cf4",
           "0xFf3Da7D04501fEBaeFC2a51Dd384cA19e76a3b5f",
           "0x8cfb1D4269f0daa003CDEa567aC8f76c0647764a",
           "0x8fc8AA0ac524B31ddF0F5Ee6331fAE02550AE266",
           "0xCa2c6d1AeFC0d5aA4c0c126f5ca6f890f9ea3343", #SECTOKEN Node
           "0x2Ed7E9fCd3c0568dC6167F0b8aEe06A02CD9ebd8",
           "0x1D20Bcf14F859A9050d64fF5AC8A99cD04287067",
           "0xdd7f964B149dE8417BBcBC6EeE4813BD444eee53",
           "0xd0328a8CCE8f9db3d8E4Ffbe2e2Bc5437Cc60a50",
           "0x38b6ab6B9294CCe1Ccb59c3e7D390690B4c18B1A", #Prophet
           "0xbBFA656005106e32b15d5f0ea7bCff1F48f5CF8D",
           "0xdDC5BB9dE09cE6e513a752B9c8a548FE227b907B",
           "0xdDeec201571851562f3C2348f17A61c64212353e",
           "0xF3336873d78C97D0AC8C2A6f47cD489F29D583a3", #PiedmontStaking
           "0xA8049b0f1C409A58d378e0E41469E824b1BB6E73",
           "0x29e3b3c76e7ae0d681bf1a6BceE1c0E7d17DBAA9",
           "0x0CE26De826d40aC45CBDeBE0B4d174f11fb224cf", #Oraculi
           "0x0b025B4ffdbA974022c82Ee3CF49C89F6ec2D8ab",
           "0x30DB581cEd950dc0052Ecc9760dE1C268A9338eC",
           "0x83dA1beEb89Ffaf56d0B7C50aFB0A66Fb4DF8cB1",
           "0x737cA98d12065C5Bb62F0C91C86cFd7548Cf7c50", #Off chain data
           "0x539DA19cD6feEc5697a1a04DbC600E55a91C78D0",
           "0xE3cd128883f2954D78923487B67Ea7C4F25C7C46",
           "0xF3b450002C7Bc300eA03c9463d8E8BA7f821b7c6",
           "0x893b163e7DdB4D050Bb5FA946FC71B505C28a6C6", #NeroNet
           "0x9E9711208e08277048bd742f6e06ca272C59d9Db",
           "0xf540C744e819aABDAAA4dD982Dbd00CcE3e26a91",
           "0x0740f15580678e9d28E6BE678cf330E46EC9eAEE",
           "0x09eCD0b83D1539e24f481d7D9644374925DF846C", #MrmChain
           "0x36a0Ee3abF799D89D689eD8fbb008b2619c7F1ab",
           "0x136C76c6752f7752Da8957B554895A13906212af",
           "0x48cd134B6225E23DFbF81E54b023231BA005B364", #LuxNode
           "0x6A7438e208fA022C4C8a71BF1e4aa2D59EDf6a2c",
           "0x240BaE5A27233Fd3aC5440B5a598467725F7D1cd",
           "0x7A9d706B2A3b54f7Cf3b5F2FcF94c5e2B3d7b24B",
           "0x1667df009ee0759c94172AE4Ecda9801607508D7", #LeviNode
           "0x7A438cbbEA99DFc73158765570B4330955d48Aed",
           "0xDdaffcBeB95d095227043fEE74062ac56Df5cbB2",
           "0xe433F992F2d282d63a1F1acC54d4B37D9546F819",
           "0x63946A61C0B0c13Ae140A87E0ebaF47cbd8d2bA4",
           "0x8c85a06EB3854Df0d502B2b00169DBfB8B603Bf3",
           "0x504b43e12Ef8b025D78e2f752B0fe20b84576A6e", #Joswig Solutions
           "0xb220D022EF8655Cb4AafA193db2BbEEf9064B1d0",
           "0x93763E0cf5828226ecC8027f1b6f7536eEe84294",
           "0x053c779ACf94aE25D059A4680806dfC718b1295a",
           "0x2Bd355065fE6b4Df4CE7c12f15b9a9b2a8392037",
           "0x2587B47e53a02789F986E9a7e837fE5879f1fe30",
           "0xdCDD8Cb3d4E7332C404772dBFE83C583D17fe821", #GeoDB
           "0x286C84CAdb3e2929F6DE5CE0AF837f5F6ee52B4C",
           "0xfdB313AAF5Ee0EAc9B85d27D3b9BDc22ae3B3cfe",
           "0xE98dFc0C36408b54326Fa11235D573574B1e8eC3",
           "0x992Ef8145ab8B3DbFC75523281DaD6A0981891bb",
           "0x049Bd8C3adC3fE7d3Fc2a44541d955A537c2A484",
           "0xE7e1B9fB5B9c5c656eC50Ea527A6779DEcCD7198", #Fibus.io
           "0x85aEace84a130bC1AcCcE2a9F4F933F6765b0B9B",
           "0xD0321ee623baB806C03f7ed2F746d0A2F2eb1857",
           "0xBfF8Bd40f4D4C4C3Db3096CcF747be967075A3D9",
           "0x54EEF5235F07AE802944F60eF5a9C0bC862C0610",
           "0x1422425b12c46235Cd89582Ba8cd4e44B0EF07E5",
           "0x45408418eA69238376fCDa67245d12751Eff5Deb", #Easy2 stake
           "0xECcB8F881cE2552EdA4115a162ffE2666B601c33",
           "0x7872eb21639Ae8193f1AAF495B967202713C8Fe5",
           "0xE7511040e264bB8857FB17078586BfFbD4E5f319", #digisense
           "0x95b00984a9c38417cDBa9653CE4F4A0A3e54451c",
           "0x8c2C80DE69d1579C6B7d60c34ebF2629d74ff60d",
           "0x475585efd6E684BeA22D0e55Ff8667B836048435",
           "0x31078d6dc2B7Ac38C2Ce2b64F5F8A37Fc193A6ba",
           "0x480414dE67277fd87b855a8Ab069cE47582a5E77",
           "0xe3fb704e96643Fe1e6f85E645A1D4DBE76F08908",
           "0xd43137De4AA10A400b0e3C97450A3c7ED52Eca1d", #Cryptonians.dev
           "0x0Ce0224ba488ffC0F46bE32b333a874Eb775c613",
           "0x2861cE140A164E5337fEDf2DA83c196b24a5A104",
           "0xAcB07C9f9b0FEC39FD0F305FbA69A26b5772f81A",
           "0x27FBD3f6Ce8def73660b1474dfB75B682AF24B66", #Chicago chainlink node ops ?
           "0xfD6A8d5b796EF2F748Ca2B7909298305cb6C6468",
           "0x703DE18e964a1F7D605E1f608c24E408013d918d",
           "0xfc5F20476E6289c7120A89D45e383EB28603152f",
           "0xF5a3d443FccD7eE567000E43B23b0e98d96445CE", #chainLayer
           "0x4565300C576431e5228e8aA32642D5739CF9247d",
           "0xC4Da88C4AFc2823410941b2A490e90C78549F3E8",
           "0x852F9B94a29bA96d94556cf9Ddd59796543EC884", #Catena
           "0x8612DDeCD801DBD1e3A8FA59e424E6E9fe6d06F2",
           "0x0650012e5E21846451100CB5406B7BA90C8D5626",#borinquen
           "0x0A39479Cc18b1c03D27D1e4A783C63754b75213d", #bookmaker ratings
           "0x0669e808B06Ba1F7a50c80cFCC44A96007bE950E",
           "0xe7013C7f42bDc073eBAC84A1982D683038888996",
           "0xF7CC0DE5d25A3921Ea502d09c5eDA9a6a3067360",
           "0x7a7AefA6aD1ADDe66b463aE54738dB8C7b7c3267", #bibex
           "0x737424BfEf17e9883b57Ee17dE230523E871C5F5",
           "0x88AD5C3A2Ef62fF0231A5Ad78464E838d6e9a971",
           "0x9308B0Bd23794063423f484Cd21c59eD38898108",
           "0xA0a3C08eF9C65Af92Ee6eFA1A9d69f06E669c985",
           "0x72f3dFf4CD17816604dd2df6C2741e739484CA62", #alphaChain
           "0xf57dA1a15B1d8B84003942F9e2f942695dEA5b3c",
           "0xe0410d161BceE12F398A3d4BE450F8B1212925Ea",
           "0xf413725017Ee57176A02158365B483698Bc432C6",
           "0xEc77e8d3a63D4AC8341dF6Ef4E07d2866fCa83D6",
           "0x64Fd0aBd4d8F5A0A7502C0078d959E57ca1207aB", #01node
           ]

start_block = 12250000
end_block = 12400000
# mind the API KEY (end of url)

data = pd.DataFrame()

for k in address:
    time.sleep(1)
    for i in range(end_block, start_block, -2000):
        time.sleep(1)
        url = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + k + \
              "&startblock=" + str(i - 2000) + "&endblock=" + str(
            i) + "&sort=desc&apikey=V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC"

        response = requests.get(url, verify = certifi.where())

        address_content = response.json()
        print(address_content)

        result = address_content.get("result")

        for transaction in result:
            block_no = transaction.get("blockNumber")
            timestamp = transaction.get("timeStamp")
            hash = transaction.get("hash")
            tx_from = transaction.get("from")
            contract_address = transaction.get("contractAddress")
            tx_to = transaction.get("to")
            value = transaction.get("value")
            tokenName = transaction.get("tokenSymbol")
            token_decimal = transaction.get("tokenDecimal")
            tansaction_index = transaction.get("transactionIndex")
            gas = transaction.get("gas")
            LINK_value = Decimal(value) / Decimal("1000000000000000000")  # calculation to LINK
            gas_price = transaction.get("gasPrice")
            gas_used = transaction.get("gasUsed")
            transaction_fee = Decimal(gas_price) * Decimal(gas_used) / Decimal("1000000000000000000")
            cumulativeGasUsed = transaction.get("cumulativeGasUsed")
            input_trans = transaction.get("Input")

            data_new = pd.DataFrame(
                {
                    'block_no': [block_no],
                    'timestamp': [timestamp],
                    'hash': [hash],
                    'tx_from': [tx_from],
                    'contract_address': [contract_address],
                    'tx_to': [tx_to],
                    'value': [value],
                    'tokenName': [tokenName],
                    'token_decimal': [token_decimal],
                    'tansaction_index': [tansaction_index],
                    'gas': [gas],
                    'LINK_value': [LINK_value],
                    'gas_price': [gas_price],
                    'gas_used': [gas_used],
                    'transaction_fee': [transaction_fee],
                    'cumulativeGasUsed': [cumulativeGasUsed],
                    'input': [input_trans]
                }
            )

            data = pd.concat([data, data_new])

print(data)

data.to_csv("C:/Users/kalin/Documents/UZH Master Thesis/data etherscan/oracles_data.csv")

