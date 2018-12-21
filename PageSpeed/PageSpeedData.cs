using System;
using System.Collections.Generic;
using System.Text;

namespace PageSpeedApi
{
    class PageSpeedData
    {
        public string captchaResult { get; set; }
        public string kind { get; set; }
        public string id { get; set; }
        public int responseCode { get; set; }
        public string title { get; set; }
        public Rulegroups ruleGroups { get; set; }
        public Loadexp loadingExperience { get; set; }
        public Pagestats pageStats { get; set; }
        public Formattedresults formattedResults { get; set; }
    }

    class Rulegroups
    {
        public SPEED SPEED { get; set; }
    }

    class SPEED
    {
        public int score { get; set; }
    }

    class Loadexp
    {
        public string initial_url { get; set; }
    }

    class Pagestats
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
        public int numTotalRoundTrips { get; set; }
        public int numRenderBlockingRoundTrips { get; set; }
    }

    class Formattedresults
    {
        public string locale { get; set; }
    }
}
