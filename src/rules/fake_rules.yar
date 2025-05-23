rule Fake_Malware_Detector
{
    meta:
        author = "YourName"
        description = "Detects fake malware strings for testing"
        date = "2025-04-11"

    strings:
        $malware1 = "BAD_MALWARE_SIGNATURE"
        $malware2 = "TROJAN_ATTACK"

    condition:
        any of them
}
