using System;
using System.Collections.Generic;
using System.Text;

namespace PageSpeedApi
{
    public class PageSpeedData
    {
        public string kind { get; set; }
        public string id { get; set; }
        public int responseCode { get; set; }
        public string title { get; set; }
        public Rulegroups ruleGroups { get; set; }
        public Pagestats pageStats { get; set; }
        public Formattedresults formattedResults { get; set; }
        public Version version { get; set; }
    }

    public class Rulegroups
    {
        public SPEED SPEED { get; set; }
    }

    public class SPEED
    {
        public int score { get; set; }
    }

    public class Pagestats
    {
        public int numberResources { get; set; }
        public int numberHosts { get; set; }
        public string totalRequestBytes { get; set; }
        public int numberStaticResources { get; set; }
        public string htmlResponseBytes { get; set; }
        public string overTheWireResponseBytes { get; set; }
        public string cssResponseBytes { get; set; }
        public string imageResponseBytes { get; set; }
        public string javascriptResponseBytes { get; set; }
        public string otherResponseBytes { get; set; }
        public int numberJsResources { get; set; }
        public int numberCssResources { get; set; }
    }

    public class Formattedresults
    {
        public string locale { get; set; }
        public Dictionary<string, RuleResult> ruleResults { get; set; }
    }

    public class RuleResult
    {
        public string localizedRuleName { get; set; }
        public float ruleImpact { get; set; }
        public string[] groups { get; set; }
        public Summary summary { get; set; }
        public Urlblock[] urlBlocks { get; set; }
    }

    public class Summary
    {
        public string format { get; set; }
        public Arg[] args { get; set; }
    }

    public class Arg
    {
        public string type { get; set; }
        public string key { get; set; }
        public string value { get; set; }
    }

    public class Urlblock
    {
        public Header header { get; set; }
        public Url[] urls { get; set; }
    }

    public class Header
    {
        public string format { get; set; }
        public Arg[] args { get; set; }
    }

    public class Url
    {
        public Result result { get; set; }
    }

    public class Result
    {
        public string format { get; set; }
        public Arg[] args { get; set; }
    }

    public class Version
    {
        public int major { get; set; }
        public int minor { get; set; }
    }
}
